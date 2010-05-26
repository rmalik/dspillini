var Y = YUI().use("test");
var testCase = new Y.Test.Case({

    //the name of the test case - if not provided, one is automatically generated
    name: "Array Tests",
    
    //-------------------------------------------------------------------------
    // Setup and teardown
    //-------------------------------------------------------------------------

    /*
     * The setUp() method is used to setup data that necessary for a test to
     * run. This method is called immediately before each test method is run,
     * so it is run as many times as there are test methods.
     */
    setUp : function () {        
        this.data = new Array (0,1,2,3,4,5);        
    },
    
    /*
     * The tearDown() method is used to clean up the initialization that was done
     * in the setUp() method. Ideally, it should free up all memory allocated in
     * setUp(), anticipating any possible changes to the data. This method is called
     * immediately after each test method is run.
     */
    tearDown : function () {
        delete this.data;
    },
    
    //-------------------------------------------------------------------------
    // Basic tests - all method names must begin with "test"
    //-------------------------------------------------------------------------
    
    /*
     * Test the push() method.
     */
    testPush : function() {
    
        //shortcut variables
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        this.data.push(6);
    
        //array-specific assertions
        ArrayAssert.isNotEmpty(this.data, "Array should not be empty.");
        ArrayAssert.contains(6, this.data, "Array should contain 6.");
        ArrayAssert.indexOf(6, this.data, 6, "The value in position 6 should be 6.");
        
        //check that all the values are there
        ArrayAssert.itemsAreEqual([0,1,2,3,4,5,6], this.data, "Arrays should be equal.");        
        
    },
    
    /*
     * Test the pop() method.
     */
    testPop : function() {
    
        //shortcut variables
        var Assert = Y.Assert;
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        var value = this.data.pop();
        
        //array shouldn't be empty
        ArrayAssert.isNotEmpty(this.data, "Array should not be empty.");                
    
        //basic equality assertion - expected value, actual value, optional error message
        Assert.areEqual(5, this.data.length, "Array should have 5 items.");
        Assert.areEqual(5, value, "Value should be 5.");   
        
        ArrayAssert.itemsAreSame([0,1,2,3,4], this.data, "Arrays should be equal.");                                
    },
    
    /*
     * Test the reverse() method.
     */
    testReverse : function() {
    
        //shortcut variables
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        this.data = this.data.reverse();
        
        ArrayAssert.itemsAreEqual([5,4,3,2,1,0], this.data, "Arrays should be equal.");                              
    },
    
    /*
     * Test the shift() method.
     */
    testShift : function() {
    
        //shortcut variables
        var Assert = Y.Assert;
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        var value = this.data.shift();
    
        //array shouldn't be empty
        ArrayAssert.isNotEmpty(this.data, "Array should not be empty.");                
    
        //basic equality assertion - expected value, actual value, optional error message
        Assert.areEqual(5, this.data.length, "Array should have 6 items."); 
        Assert.areEqual(0, value, "Value should be 0."); 
        
        ArrayAssert.itemsAreEqual([1,2,3,4,5], this.data, "Arrays should be equal.");                              
    },            
    
    /*
     * Test the splice() method.
     */
    testSplice : function() {
    
        //shortcut variables
        var Assert = Y.Assert;
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        var removed = this.data.splice(1, 2, 99, 100);
    
        //basic equality assertion - expected value, actual value, optional error message
        Assert.areEqual(6, this.data.length, "Array should have 6 items.");              
    
        //the new items should be there
        ArrayAssert.indexOf(99, this.data, 1, "Value at index 1 should be 99.");   
        ArrayAssert.indexOf(100, this.data, 2, "Value at index 2 should be 100.");   
        
        ArrayAssert.itemsAreEqual([0,99,100,3,4,5], this.data, "Arrays should be equal.");  
        ArrayAssert.itemsAreEqual([1,2], removed, "Removed values should be an array containing 1 and 2.");

    },

    /*
     * Test the unshift() method.
     */
    testUnshift : function() {
    
        //shortcut variables
        var Assert = Y.Assert;
        var ArrayAssert = Y.ArrayAssert;
    
        //do whatever data manipulation is necessary
        this.data.unshift(-1);
    
        //basic equality assertion - expected value, actual value, optional error message
        Assert.areEqual(7, this.data.length, "Array should have 7 items."); 

        //the new item should be there
        ArrayAssert.indexOf(-1, this.data, 0, "First item should be -1."); 
    
        ArrayAssert.itemsAreEqual([-1,0,1,2,3,4,5], this.data, "Arrays should be equal.");                              
    } 
    
});

Y.Test.Runner.add(testCase);
Y.Test.Runner.run();