<template>
      <div id="register" style="display: flex;justify-content: center;" >
    <title>Title</title>
    <meta charset="utf-8">




          <!--设立一个div-->
          <div>
              <h2>注册</h2>
              <br>
              <!--input的应用-->
              <label>用户名称</label>
              <input v-model="username" placeholder="用户名称"><br><br>
              <label>密码</label>
              <input v-model="password" type="password" placeholder="输入密码"><br><br>
              <label>重复输入密码</label>
              <input type="password" v-model="rePassword" placeholder="重复输入密码"><br><br>
              <label>性别</label>
              <input type="radio" id="male" value="male" v-model="sex">
              <label for="male">male</label>
              <input type="radio" id="female" value="female" v-model="sex">
              <label for="female">female</label><br><br>
              <label> 电子邮箱 </label>
              <input v-model="email" placeholder="请输入邮箱" ><br><br>
              <label> 手机号码 </label>
              <input v-model="phonenumber" placeholder="请输入手机号码" @keyup.enter="submit"><br><br>
              <!--
              <label>爱好</label>
              <input type="checkbox" id="basketball" value="蓝球" v-model="hobby">
              <label for="basketball">篮球</label>
              <input type="checkbox" id="football" value="足球" v-model="hobby">
              <label for="football">足球</label>
              <input type="checkbox" id="other" value="其他" v-model="hobby">
              <label for="other">其他</label><br><br>
              <label>职业</label>
              <select v-model="work">
                  <option disabled value="">请选择</option>
                  <option>学生</option>
                  <option>工作</option>
                  <option>其他</option>
              </select><br><br>
              <label>备注</label>
              <textarea v-model="note" placeholder="备注"></textarea><br><br>
              -->
              <button v-on:click="submit" >提交</button>
          </div>
      </div>
</template>
 
<script>
export default {
  name: 'register',
  data () {
    return {
              username: '',
              password: '',
              rePassword: '',
              email: '',
              sex: '',
              phonenumber: '',
              uid:"",
    }
  },
            methods: {
              submit() {
  
                  if(this.username.length<1)
                  {
                      alert("用户名不能为空！");
                  }
                  else
                  if(this.sex.length<1)
                {
                  alert ("性别不得为空！")
                }
                else
                  {
                  if(this.phonenumber.length!=11&&!/^0?1[3|4|5|6|7|8][0-9]\d{8}$/.test(this.phonenumber))//检验了开头前两位，固定数字和11位
                  {
                      alert("手机号应为11位数字！")
                  }
                  else
                  if(this.email.length<1)
                  {
                    alert("电子邮箱不得为空！")
                  }
                  else

                  if (this.password === this.rePassword) {
                    if(this.password.length>5)
                    {
                      let con = confirm("用户名：" + this.username + ' 性别：' +
                          this.sex + '电子邮箱：' +this.email);
                      if (con) alert("注册成功");
                      else alert("取消提交");
                    }
                    else
                    {
                      alert("密码不得小于六位！")
                    }
                  }else {
                      alert("两次密码输入不一致！")
                  }
                  }
                  //检测用户名已存在还没做
              }
            }

}
</script>