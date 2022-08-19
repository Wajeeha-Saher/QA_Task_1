Feature: Test-EndPoints

 
     Scenario: Verify the response of Get list users
       Given the user is on base url
       When we hit the Get_List_Users api
       Then the list of users is returned 

     Scenario Outline: Verify the response of Get single users
       Given the user is on base url
       When we hit the <Get_single_user> api for users
       Then the <Get_single_user> is returned 
       Examples:
       | Get_single_user |
       | Get_Single_User_found |
       | Get_Single_User_NotFound |

    Scenario Outline: Verify the response of Get Resources
      Given the user is on base url
      When we hit the get <Resource> api for resources
      Then the <Resource> is returned as response
      Examples:
      | Resource |
      | Get_List_Resource |
      | Get_Single_Resource_Found |
      | Get_Single_Resource_NotFound |

      Scenario: Verify the response of Create user
        Given the user is on base url
        When we hit the Create user api
        Then the user is created successfully 

     Scenario: Verify the response of Update user
       Given the user is on base url
       When we hit the Update user api
       Then the user is Updated successfully 

     Scenario: Verify the response of Delete user
       Given the user is on base url
       When we hit the Delete user api
       Then the user is Deleted successfully 

     Scenario Outline: Verify the response of Register
       Given the user is on base url
       When we hit the <Register> user api
       Then the user <Register> succ/unsucc
       Examples:
       | Register |
       | Register_User_Successfully |
       | Register_User_UnSuccessfully |

    Scenario Outline: Verify the response of User Login
      Given the user is on base url
      When we hit the user <Login> api
      Then the user will <Login>
      Examples:
      | Login |
      | User_Login_Successfully |
      | User_Login_UnSuccessfully |

    Scenario: Verify the Delayed response
       Given the user is on base url
       When we hit the get api for response
       Then delay response is returned 



  

 