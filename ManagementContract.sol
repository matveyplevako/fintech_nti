pragma solidity ^0.4.20;

import "./contracts/math/SafeMath.sol";
import "./contracts/ownership/Ownable.sol";
import "./myERC721Token.sol";

contract ManagemetContract is Ownable {
    using SafeMath for uint;
    
    uint fee;
    uint MerchCount = 0;
    
    mapping(bytes32 => address) public CompanyAddresses;
    mapping(address => string) public TokenCompanyAddresses;
    mapping(bytes32 => uint) public MerchId;
    mapping(uint => address) public MerchAddress;
    mapping(address => string) public MerchName;
    
    event newVendorOwnedToken(address);
    
    function regVender(string full, string short) payable public {
        require(msg.value >= fee);
        require(CompanyAddresses[keccak256(full)] == 0x0);
        Token TokenAddress = new Token(this, msg.sender, full, short);
        emit newVendorOwnedToken(TokenAddress);
        CompanyAddresses[keccak256(full)] = TokenAddress;
        TokenCompanyAddresses[TokenAddress] = full;
    }
    
    function regMerch(string name) public {
        require(keccak256(MerchName[msg.sender]) == keccak256("") &&
        keccak256(name) != keccak256("") &&
        MerchId[keccak256(name)] == 0);
        MerchCount = MerchCount.add(1);
        MerchId[keccak256(name)] = MerchCount;
        MerchAddress[MerchCount] = msg.sender;
        MerchName[msg.sender] = name;
    }
    
    function setFee(uint price) public onlyOwner {
        fee = price;
    }
    
    function getFee() public view returns(uint) {
        return fee;
    }
    
    function ManagemetContract() public {
        setFee(0.5 ether);
    }
    
}