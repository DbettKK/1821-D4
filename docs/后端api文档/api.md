# API文档

##### 简要描述

- 用户注册接口

##### 请求URL
- ` http://175.24.121.113:8000/myapp/register `
  
##### 请求方式
- POST 

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|username |是  |string |用户名   |
|password |是  |string | 密码    |
|password2 |是  |string | 重复密码 |
|email     |是  |string | 邮箱    |
|phone_num     |是  |string | 手机号    |

##### 返回示例 

``` 
{
    "info": "success",
    "code": 200,
    "data": {
        "id": 13,
        "username": "刘六",
        "email": "12@12.12",
        "phone_num": "12345678911"
    }
}
```

##### 返回参数说明 

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|info |string   |信息，可能成功或者失败原因  |
|code |int   |返回状态码，200 400  |
|data |dic   |注册的用户完整信息  |

##### 备注 

- 更多返回错误代码请看首页的错误代码描述