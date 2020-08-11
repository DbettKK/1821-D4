<template>
  <div class="login_container">
    <div class="login_box">
      <div class="avatar_box">
        <img src="../../assets/logo.png" alt="">
      </div>
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
        <el-form-item prop="username">
          <el-input placeholder="请输入账号" v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input placeholder="请输入密码" v-model="loginForm.password" prefix-icon="el-icon-lock" type="password"></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button type="primary" @click="login">登录</el-button>
          <el-button type="info" @click="resetloginForm">重置</el-button>
          <el-form-item><router-link to="/register" class=a>还未拥有账号？前往注册</router-link></el-form-item>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },

      loginFormRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 2, max: 15, message: '长度在 6 到 15 个字符', trigger: 'blur' }
          // 因为数据库现在存的都是简单密码。。所以这里min先改成2，之后再改回来
        ]
      }
    }
  },
  //保存登录状态
  
  //created() {
    //console.log(sessionStorage.getItem("store"));
    //console.log(sessionStorage.length);
    // 如果sessionStorage中存储了store
    //if (sessionStorage.getItem("store")) {
      // replaceState 替换state根状态（参数为 对象）
      //this.$store.replaceState( Object.assign({}, this.$store.state, JSON.parse(sessionStorage.getItem("store")))) 		                                         
    //}
    //在页面刷新时将vuex里的信息保存到sessionStorage里
    //window.addEventListener("beforeunload",()=>{
        //sessionStorage.setItem("store", JSON.stringify(this.$store.state))
    //})
  //},
  
  methods: {
    //exit(){
      //console.log(this.$store.state.token)
      //this.$store.commit('exit')
      //console.log(this.$store.state.token)
    //},
    resetloginForm () {
      // console.log(this)
      this.$refs.loginFormRef.resetFields();
    },
      login () {
          this.$refs.loginFormRef.validate(async (valid) => {
              if (!valid) return false;
              // 缺少请求路径login

              const { data: res } = await this.$http.post('http://175.24.121.113:8000/myapp/login/',
                  this.$qs.stringify(this.loginForm));
              console.log(res);
              if (res.code !== 200) return console.log('登录失败');
              // 这里后端返回了一个code就先用code看看效果
              else{
                console.log('登录成功');
                window.sessionStorage.setItem("token", res.token);
                this.$router.push('/')
              }

              // this.$http.post('http://175.24.121.113:8000/myapp/login/',
              //     this.$qs.stringify(this.loginForm)
              // ).then(function (res) {
              //     console.log(res.data)
              // }).catch(function (error) {
              //     console.log(error)
              // });
          });
      }

  }
}
</script>

<style lang="less" scoped>
.login_container {
  background-color: rgb(0, 194, 129);
  height: 100%;
}

.login_box {
  width: 450px;
  height: 300px;
  background-color: #fff;
  border-radius: 3px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);

  .avatar_box {
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background-color: #eee;
    }
  }

  .login_form {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
  }

  .btns {
    display: flex;
    justify-content: flex-end;
  }
  .a{
        text-decoration: none;
        color:#333;
    }
}
</style>
