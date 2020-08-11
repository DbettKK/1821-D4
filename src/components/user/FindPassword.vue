<template>
  <div class="login_container">
    <div class="login_box">
      <div class="avatar_box">
        <img src="../../assets/logo.png" alt="">
      </div>
      <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="100px" class="login_form">
        <el-form-item  label="用户名" prop="username">
          <el-input v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="loginForm.email" prefix-icon="el-icon-lock"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="password">
          <el-input v-model="loginForm.password_new" prefix-icon="el-icon-lock" type="password"></el-input>
        </el-form-item>
        <el-form-item label="验证码" prop="code">
          <el-input v-model="loginForm.code" prefix-icon="el-icon-lock"></el-input>
        </el-form-item>
        <el-form-item class="btns">
          <el-button style="margin-right:10px" type="primary" @click="sendEmail">获取验证码</el-button>
          <el-button type="primary" @click="submitForm">找回密码</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import QS from "qs";
import Vue from 'vue'
export default {
    name: "FindPassword",
  data () {
      //很大程度参照了login的写法
    return {
      loginForm: {
        username: '',
        email: '',
        password_new: '',
        code: ''
      },

      loginFormRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur' }
        ],
         password_new: [
          {
            required: true,
            message: "密码不能为空。",
            trigger: "blur"
          },
          {
            min: 6,
            max: 20,
            message: "密码必须介于6-20个字符之间。",
            trigger: "blur"
          },
          {
            type: "string",
            pattern: /^[a-zA-Z0-9_-]{6,20}$/,
            message: "格式不正确。",
            trigger: "blur"
          }
        ],
        email: [
          {
            //required: true,
            message: "此处不能为空。",
            trigger: "blur"
          },
          {
            max: 50,
            message: "此处不能大于50个字符。",
            trigger: "blur"
          },
          {
            type: "string",
            pattern: /(^(\w-*\.*)+@(\w-?)+(\.\w{2,})+)|(1\d{10})$/,
            message: "格式不正确。",
            trigger: "blur"
          },
        ],
        code: [
          {
            len: 16,
            message: "验证码必须是16个字符。",
            trigger: "blur"
          },
        ]
      }
    }
  },
  
  methods: {
    sendEmail() {
      Vue.axios
        .post('http://175.24.121.113:8000/myapp/email2/', QS.stringify(this.loginForm))
        .then(response => {
              if (response.data.emailed) {
                // 发送成功
              //  this.$router.replace("/");
                this.$message({
                    message: "发送成功",
                    type: "success",
                    customClass: "c-msg",
                    showClose: true
                  }); 
              } else {
                // 发送失败
                this.isSuccess = false;
                  this.$message({
                    message: "发送失败",
                    type: "error",
                    customClass: "c-msg",
                    showClose: true
                  }); 
              }
          })
        .catch(error => {
              this.$message({
                message: "该页面出了点状况",
                type: "error",
                customClass: "c-msg",
                duration: 0,
                showClose: true
              });
              Promise.reject(error);
            });
    },
    submitForm() {
      this.$refs.loginFormRef.validate(valid => {
        if (valid) {
          // 指定请求为正式提交表单
          Vue.axios
            .post('http://175.24.121.113:8000/myapp/findpassword/', QS.stringify(this.loginForm))
            .then(response => {
              if (response.data.registered) {
                // 注册成功
                this.$router.replace("/");
                this.$message({
                    message: response.data.username,
                    type: "success",
                    customClass: "c-msg",
                    showClose: true
                  }); 
              } else {
                // 注册失败
                  this.$message({
                    message: response.data.info,
                    type: "error",
                    customClass: "c-msg",
                    showClose: true
                  }); 
              }
            })
            .catch(error => {
              this.$message({
                message: "该页面出了点状况",
                type: "error",
                customClass: "c-msg",
                duration: 0,
                showClose: true
              });
              Promise.reject(error);
            });
        }
        return false;
      });
    },

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
  height: 550px;
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
    justify-content: flex-start;
  }
}
</style>

