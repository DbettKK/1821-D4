<template>
    <el-container class="Info_Container">
        <el-container class="Inner_container">
            <el-aside width="30%">
                <div class="Inner_aside">
                    <img src="../../assets/logo.png" alt=""  width="70%" height="50%">
                    <p>用户信息与修改</p>
                </div>
            </el-aside>
            
            <el-main>
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="用户">
                        <el-input v-model="form.name" prefix-icon="el-icon-user-solid" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="form.pwd" prefix-icon="el-icon-key" type=password></el-input>
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
                    <el-button type="info" round @click="ChangeInfo">确认修改</el-button>
                </el-form>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
export default {
    data(){
        return {
            form: {
                name: 'Y',
                pwd: '156as4d8e',
                phone: '17812112605',
                email:'ema.buaa.edu.cn',
                type: '普通用户',
                ID: '115099'
            }
        }
    },
    watch:{

    },
    methods:{
        ChangeInfo(){
            this.$prompt('请输入旧密码', '信息修改', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
            }).then(({ value }) => {
            this.$message({
                type: 'success',
                message: '密码修改成功'
            },
            console.log(value));
            }).catch(() => {
            this.$message({
                type: 'info',
                message: '取消输入'
            });       
            });
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
</style>