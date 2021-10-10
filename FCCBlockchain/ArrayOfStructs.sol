pragma solidity ^0.6.0;

contract SimpleStorage
{
    // using a structs
    // define new types in solidity
    uint256 favoriteNumber; 
    bool favoriteBool;
    bool favoriteBool2;
    // each of them are at different indices 
    
    
    struct People
    {
        uint256 favoriteNumber;
        string name;
        
    }
    
    // Array of structs 
    // Array: way of storing sometihg
    
    People[] public people; // this is a dynamic array 
    
    // we can also create an array of fixed size 
    
    //Fixed arrays don't change size 
    
    People[1] public peoplestatic;
    
    //People public person = People({favoriteNumber: 2, name: "Patrick Collins"});
    
    function store( uint256 _favoriteNumber ) public 
    {
        favoriteNumber= _favoriteNumber;
    }
    
    
    function retrieve() public view returns (uint256)
    
    {
        return favoriteNumber;
    }
    
    
    function addPerson(string memory _name, uint256 _favoriteNumber) public
    {
        // way to add person to an array 
        
        people.push(People({favoriteNumber:_favoriteNumber,name: _name}));
        
    }
    
}
