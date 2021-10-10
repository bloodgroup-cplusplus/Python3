//define your solidity version 

pragma solidity ^0.6.0;

// we wanna use anything between 0.6 and 0.9 

// we need to go to the compiler so that we compile with the newer version 

// we define our contract 
//contract is a keyword in solidity similar to class 


contract SimpleStorage 
{
    // contents of contract for simple storage 
// we can hypothetically deploy this now 

    // we can have integers 
    //uint , int, unit256, 
    // if we add public we can view our number (favorite number )
    uint256 public  favoriteNumber;
    // this is an integer of size 256 bits 
    // we can also do other stuffs
    // we can also have booleans 
   /* bool favoriteBool = true; 
    
    string gavoriteString = "String";
    
    int256 favoriteInt = -7;
    
    address  favoriteAddress = 0x71c7656ec7ab88b098defb751b7401b5f6d8976f;
    
    bytes32 favouriteByes = "cat";
    
    */
    // if we don't initialize it will be initialized to a null value 
    
    // unit256 favuriteNumber; this is zero 
    
    // let's create our first functions 
    
    // this function changes the value of our favourite number 
    
    // there are four different types of visibility in solidity 
    // external public internal and private 
    
    // we are mostly going to work with pubic 
    // public functions/varialbes can be called by anyone 
    //external funtion can only be called for 
    
    function store(uint256 _favoriteNumber) public{
        favoriteNumber = _favoriteNumber;
    } 
    // for instance if our function was external instead of being pubic we couldn't call 
    // store inside the function itself
    
    // this is not allowed as the function is external 
    // you cannot call the function inside
    /*
    function store(uint256, _favoriteNumber) external {
        favoriteNumber = _favoriteNumber;
        store();
    }
        
    // however internal functions can only be called inside the given functions
    
    // for instance if we have an internal function we call do this
    
    */
   // function sotre(uint256, _favoriteNumber) internal {
      //  favoriteNumber = _favoriteNumber;
       // store();
    // this is totally valid
    
    // whenever you make a state change we are also making a transactions
    
    // The reason 
    
    
    function retrieve() public view returns (uint256)
    {
        return favoriteNumber;
    }
    
    // why is the store orange and favouriteNumber and retrieve blue
    // the answer is  the key lies in the view functions
    // View and pure 
    // View means we want to read some state of the blockchain
    // If we are reading off of blockchain we are not making state change 
    // We don't need to make any transactions
    // These public variables automatically blue 
    // Public are technically view functions
    // Pure funtions that purely do one task of math 
    
    // we do  the math but we do not save the state
    
    // The reason that nothing shows up in the bottom 
    // In order for functions to give something 
    // we  need to define what we going to return
    
    function retrieve() public view returns(uint256)
    {
        return favouriteNumber;
    }
    
    
    }
}
