<template>
    <el-container class="Info_Container">
        <el-container class="Inner_container">
            <el-aside width="30%">
                <div class="Inner_aside">
                    <img src="../../assets/logo.png" alt=""  width="70%" height="50%">
                    <p>用户信息与修改</p>
                </div>
            </el-aside>
            <el-divider direction="vertical"></el-divider>
            <el-main>
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="用户">
                        <el-input v-model="form.name" prefix-icon="el-icon-user-solid" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="form.password" prefix-icon="el-icon-key" type=password></el-input>
                    </el-form-item>
                    <el-form-item label="手机">
                        <el-input v-model="form.phone" prefix-icon="el-icon-phone" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="邮箱">
                        <el-input v-model="form.email" prefix-icon="el-icon-s-promotion" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="权限">
                        <el-input v-model="form.type" prefix-icon="el-icon-unlock" :disabled="true"></el-input>
                    </el-form-item>
                    <el-form-item label="ID">
                        <el-input v-model="form.ID" prefix-icon="el-icon-user" :disabled="true"></el-input>
                    </el-form-item>
                    <div>
                        <el-button type="info" round @click="dialogFormVisible=true">确认修改</el-button>
                        <el-button type="return" round><router-link to="/" class="a">返回</router-link></el-button>
                    </div>
                    <el-dialog title="修改信息" :visible.sync="dialogFormVisible" width="400px">
                        <el-form :model="form">
                            <el-form-item label="原始密码" :label-width="formLabelWidth">
                                <el-input v-model="form.old_pwd" prefix-icon="el-icon-key" show-password></el-input>
                            </el-form-item>
                            <div>
                                <el-button @click="dialogFormVisible = false">取 消</el-button>
                                <el-button type="primary" @click="CheckPwd">确 定</el-button>
                            </div>
                        </el-form>
                    </el-dialog>
                </el-form>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
//import QS from "qs";
import Vue from 'vue'
export default {
    name: "Userinfo",
    data(){
        return { 
            form: {
                name: 'Y',
                password: '136671zxc',
                phone: '',
                email:'',
                type: '普通用户',
                ID: 11,
                token:'',
                old_pwd:''
            },
            dialogFormVisible: false,
            formLabelWidth: '80px'
        }
    },
    created: function(){
        this.token=window.sessionStorage.getItem('token');
        this.GetInfo();
    },
    watch:{

    },
    methods:{
        CheckPwd(){
            console.log('old_password='+this.form.old_pwd);
            Vue.axios.post(
                'http://175.24.121.113:8000/myapp/user/modify/',
                this.$qs.stringify({
                    old_password: this.form.old_pwd
                }),
                {
                    headers: {
                        'token': this.token
                    }
                }).then(res => {
                    console.log(res);
                    this.ChangeInfo();
                }).catch(res => {
                    console.log(res);
            });
        },
        ChangeInfo(){
            this.dialogFormVisible = false;
            Vue.axios.post(
                "http://175.24.121.113:8000/myapp/user/info/",this.$qs.stringify({
                    new_password:this.form.password,
                    email:this.form.email,
                    phone_num:this.form.phone
                }),
                {
                    headers: {
                        token: this.token
                    }
                }).then(function(res)  {
                    console.log(res);
                    console.log('success');
                }).catch(res => {
                    console.log(res);
            });
        },
        GetInfo(){
            Vue.axios.get(
                'http://175.24.121.113:8000/myapp/user/info',
                {
                headers:{
                    token:this.token
                    }
                }
            ).then(res=>{
                this.form.name=res.data.data.username;
                this.form.phone=res.data.data.phone_num;
                this.form.ID=res.data.data.id;
                this.form.email=res.data.data.email;
                console.log(res.data.data);
            }).catch(function(error){
                console.log(error);
            })
        }
    }
}
</script>

<style lang="less" scoped>
    .Info_Container{
        background-color:#F2F6FC;
        text-align: center;
        margin-top: 5%;
        height:85%;
        padding-left: 20%;
        padding-right: 20%;
    }
    .Inner_container{
        width: 90%;
        height: 80%;
        background-color:#FFFFFF;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        vertical-align: middle;
        margin-top: 5%;
        padding-top: 2%;
        padding-right: 20%;
        padding-left: 15%;
    }
    .Inner_aside{
        padding-top: 60%;
    }
    .el-main{
        vertical-align: middle;
        text-align: center;

    }
    .el-divider--vertical{
        display: inline-block;
        width: 1px;
        height: 400px;
        margin: 8px;
        vertical-align: middle;
        position: relative;
    }
    .a{
        text-decoration: none;
        background-color:rgb(255,255,255);
    }
</style>