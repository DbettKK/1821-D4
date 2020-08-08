<template>
    <div>
        <!-- 随便写的 -->
        <el-row>
            <el-col :span="2">用户名:</el-col>
            <el-col :span="4">
                <el-input v-model="username" placeholder="你的用户名"></el-input>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="2">密码:</el-col>
            <el-col :span="4">
                <el-input placeholder="请输入密码" v-model="userpwd" show-password></el-input>
            </el-col>
        </el-row>
        <el-row>
            <el-button type="primary" v-on:click="log" plain>登录</el-button>
        </el-row>
    </div>
</template>
<script>
import Vue from 'vue'
export default {
  data(){
      return {
        username:'',
        userpwd:''
      }
  },
  methods:{
      log(){
          Vue.axios.post('',{
              
        }).then(function(res){
            console.log(res.data.result);
        }).catch(function(res){
            console.log(res);
        })
      }
  }
}
</script>

<style>
    .el-row {
        margin-bottom: 20px;
    }
    .el-col {
        border-radius: 4px;
    }
</style>