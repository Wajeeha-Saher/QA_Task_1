
import requests
from utilities.configurations import *
from utilities.resources import *
from behave import *
from payload import *
from utilities.responses import *
from asyncio.windows_events import NULL


@given('the user is on base url')
def create_amenity(context):
    context.BaseUrl = getConfig()['API']['baseurl'] 
    print(context.BaseUrl)

@when('we hit the Get_List_Users api')
def step_impl( context):
    context.GetUserListUrl = getConfig()['API']['baseurl'] + ApiResources.GetListUsers
    context.UsersListResponse = requests.get(context.GetUserListUrl)
    context.UsersListResponseJson = context.UsersListResponse.json()
    print(context.UsersListResponseJson)
    
@then('the list of users is returned')
def step_impl(context):
    print(responses.Users_List)
    assert context.UsersListResponseJson == responses.Users_List


@when('we hit the {Get_single_user} api for users')
def step_impl( context, Get_single_user):
    if Get_single_user == 'Get_Single_User_found':
        context.GetUserUrl = getConfig()['API']['baseurl'] + ApiResources.Get_Single_User
    if Get_single_user == 'Get_Single_User_NotFound':
        context.GetUserUrl = getConfig()['API']['baseurl'] + ApiResources.Get_Single_User_NotFound
    print(context.GetUserUrl)
    context.ApiResponse = requests.get(context.GetUserUrl)
    print(context.ApiResponse)
    context.ApiResponseJson = context.ApiResponse.json()
    print(context.ApiResponseJson)
    
@then('the {Get_single_user} is returned')
def step_impl(context, Get_single_user):
    if Get_single_user == 'Get_Single_User_found':
        assert context.ApiResponseJson == responses.User_Found
    if Get_single_user == 'Get_Single_User_NotFound':
        assert context.ApiResponseJson == responses.User_NotFound


@when('we hit the get {Resource} api for resources')
def step_impl( context, Resource):
    if Resource == 'Get_List_Resource':
        context.GetResourceUrl = getConfig()['API']['baseurl'] + ApiResources.Get_List_Resource
    if Resource == 'Get_Single_Resource_Found':
        context.GetResourceUrl = getConfig()['API']['baseurl'] + ApiResources.Get_Single_Resource
    if Resource == 'Get_Single_Resource_NotFound':
        context.GetResourceUrl = getConfig()['API']['baseurl'] + ApiResources.Get_Single_Resource_NotFound
    print(context.GetResourceUrl)
    context.ApiResponse = requests.get(context.GetResourceUrl)
    print(context.ApiResponse)
    context.ApiResponseJson = context.ApiResponse.json()
    print(context.ApiResponseJson)
    
@then('the {Resource} is returned as response')
def step_impl(context, Resource):
    print(responses.User_Found)
    if Resource == 'Get_List_Resource':
        assert context.ApiResponseJson == responses.Resource_List
    if Resource == 'Get_Single_Resource_Found':
        assert context.ApiResponseJson == responses.Single_Resource_Found
    if Resource == 'Get_Single_Resource_NotFound':
        assert context.ApiResponseJson == responses.Single_Resource_NotFound


@when('we hit the Create user api')
def step_impl( context):
    context.CreateUserUrl = getConfig()['API']['baseurl'] + ApiResources.Post_Create
    print(context.CreateUserUrl)
    context.Create_User = CreateUser()
    context.ApiResponse = requests.post(context.CreateUserUrl, context.Create_User)
    print(context.ApiResponse)
    
@then('the user is created successfully')
def step_impl(context):
    print(context.ApiResponse.status_code)
    assert context.ApiResponse.status_code == 201


@when('we hit the Update user api')
def step_impl( context):
    context.UpdateUserUrl = getConfig()['API']['baseurl'] + ApiResources.Put_Patch_Update
    print(context.UpdateUserUrl)
    context.Update_User = UpdateUser()
    context.ApiResponse = requests.put(context.UpdateUserUrl, context.Update_User)
    print(context.ApiResponse)
    
@then('the user is Updated successfully')
def step_impl(context):
    print(context.ApiResponse.status_code)
    assert context.ApiResponse.status_code == 200


@when('we hit the Delete user api')
def step_impl( context):
    context.DeleteUserUrl = getConfig()['API']['baseurl'] + ApiResources.Delete
    print(context.DeleteUserUrl)
    context.ApiResponse = requests.delete(context.DeleteUserUrl)
    print(context.ApiResponse)
    
@then('the user is Deleted successfully')
def step_impl(context):
    print(context.ApiResponse.status_code)
    assert context.ApiResponse.status_code == 204


@when('we hit the {Register} user api')
def step_impl( context, Register):
    context.RegisterUserUrl = getConfig()['API']['baseurl'] + ApiResources.Post_Register
    if Register == 'Register_User_Successfully':
        context.Register_User = RegisterSuccessfulUser()
    if Register == 'Register_User_UnSuccessfully':
        context.Register_User = RegisterUnSuccessfulUser()
    print(context.RegisterUserUrl)
    print(context.Register_User)
    context.ApiResponse = requests.post(context.RegisterUserUrl,context.Register_User )
    print(context.ApiResponse)
    
@then('the user {Register} succ/unsucc')
def step_impl(context, Register):
    if Register == 'Register_User_Successfully':
         print(context.ApiResponse.status_code)
         assert context.ApiResponse.status_code == 200
    if Register == 'Register_User_UnSuccessfully':
         print(context.ApiResponse.status_code)
         assert context.ApiResponse.status_code == 400

@when('we hit the user {Login} api')
def step_impl( context, Login):
    context.LoginUrl = getConfig()['API']['baseurl'] + ApiResources.Post_Login
    if Login == 'User_Login_Successfully':    
        context.Login = LoginSuccessful()
    if Login == 'User_Login_UnSuccessfully':
        context.Login = LoginUnSuccessful()
    print(context.LoginUrl)
    context.ApiResponse = requests.post(context.LoginUrl,context.Login )
    print(context.ApiResponse)
    context.ApiResponseJson = context.ApiResponse.json()
    
@then('the user will {Login}')
def step_impl(context, Login):
    if Login == 'User_Login_Successfully':
        assert context.ApiResponse.status_code == 200
        assert context.ApiResponse.json() == responses.Login_Successful
    if Login == 'User_Login_UnSuccessfully':
        assert context.ApiResponse.json() == responses.Login_UnSuccessful
        assert context.ApiResponse.status_code == 400


@when('we hit the get api for response')
def step_impl( context):
    context.DelayedResponseUrl = getConfig()['API']['baseurl'] + ApiResources.Get_Delayed_Response
    print(context.DelayedResponseUrl)
    context.ApiResponse = requests.get(context.DelayedResponseUrl)
    print(context.ApiResponse)
    context.ApiResponseJson = context.ApiResponse.json()
   
    
@then('delay response is returned')
def step_impl(context):
    print(context.ApiResponse.status_code)
    assert context.ApiResponse.status_code == 200
    assert context.ApiResponseJson == responses.DelayedResponse

   
