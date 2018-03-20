pragma solidity ^0.4.21;


import "./contracts/math/SafeMath.sol";
import "./contracts/ownership/Ownable.sol";
import "./ManagementContract.sol";

contract Token is Ownable {
    using SafeMath for uint256;
    
    modifier onlyOwnerOf(uint256 _tokenId) {
    require(tokenOwner[_tokenId] == msg.sender);
    _;
  }
 
    struct Asset {
        string prop;
        string status;
    }
    
    ManagemetContract Manager;
    string public full_name;
    string public symbols;
    uint public Id = 0;
    event AssetCreated(uint tokenId);
    mapping(uint => address) public tokenOwner;
    mapping(uint => Asset) public Assets;
    
    function Token(address manager, address vender, string full, string short) public {
        Manager = ManagemetContract(manager);
        full_name = full;
        symbols = short;
        owner = vender;
    }
    
    function createNewId() private returns(uint) {
        Id = Id.add(1);
        return Id;
    }
    
    function transfer(string _MerchName, uint _tokenId) public onlyOwnerOf(_tokenId) {
        uint MerchId = Manager.MerchId(keccak256(_MerchName));
        _transfer(Manager.MerchAddress(MerchId), _tokenId);
    }
    
    function create(uint num) public onlyOwner {
        for (uint i = 0; i < num; i++ ) {
            _mint(createNewId());
        }
    }

    function setProperty(string prop, uint _tokenId) public  onlyOwner {
        Assets[_tokenId].prop = prop;
    }
    
    // function getProperty(uint256 _tokenId) public view returns(string[3]) {
        // string storage prop = Assets[_tokenId].prop;
        // string name = Manager.MerchName(tokenOwner[_tokenId]);
        // string storage status = Assets[_tokenId].status;
        // return [name, prop, status];
    // }
    
    function _mint(uint _tokenId) internal {
        emit AssetCreated(_tokenId);
        Assets[_tokenId] = Asset(symbols, "in operation");
        _transfer(Ownable.owner, _tokenId);
    }
    
    function _transfer(address _to, uint _tokenId) internal {
        tokenOwner[_tokenId] = _to;
    }
    
    function destroy(uint _tokenId) public {
        require(msg.sender == tokenOwner[_tokenId] || msg.sender == Ownable.owner);
        if (tokenOwner[_tokenId] == msg.sender) {
            requestBurning(_tokenId);
        } else if (Ownable.owner == msg.sender) {
            burn(true, _tokenId);
        }
    }
    
    function requestBurning(uint _tokenId) public onlyOwnerOf(_tokenId) {
        Assets[_tokenId].status = "out of use";
    }
    
    function burn(bool accepted, uint _tokenId) public onlyOwner {
        require(keccak256(Assets[_tokenId].status) == keccak256("out of use"));
        if (accepted) {
            tokenOwner[_tokenId] = 0;
            Assets[_tokenId] = Asset("", "");
        } else {
            Assets[_tokenId].status = "in operation";
        }
    }
}