<template>
    <el-container style="height: 100%; border: 1px solid #eee">
        <el-header style="text-align: right; font-size: 12px">
            <div class="name_place">
                <span class="name">金刚石文档</span>
            </div>
            <div>
                <el-dropdown trigger="click">
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item @click.native="logout">退出登录</el-dropdown-item>
                        <el-dropdown-item><router-link to="/changeinfo" class="a">修改密码及个人信息</router-link></el-dropdown-item>
                        <el-dropdown-item>注销账号</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
                <span><userinfo class="username"></userinfo></span>
            </div>
        </el-header>
        
        <el-container>
            <el-aside :width="isCollapse ? '64px' : '200px'" style="background-color: rgb(238, 241, 246)">
                <div class="toggle-button" @click="toggleCollapse">|||</div>
                <el-menu :default-openeds="['1', '3']" :unique-opened="true" :collapse="isCollapse" :collapse-transition="false" style="background-color: rgb(238, 241, 246)">
                    <el-submenu index="1" style="background-color: rgb(238, 241, 246)">
                        <template slot="title"><i class="el-icon-user-solid"></i><span>个人空间</span></template>
                        <el-menu-item-group style="background-color: rgb(238, 241, 246)">
                            <template slot="title">个人信息</template>
                            <el-menu-item index="1-1">个人详情</el-menu-item>
                            <el-menu-item index="1-2">消息通知</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="2" style="background-color: rgb(238, 241, 246)">
                        <template slot="title"><i class="el-icon-menu"></i><span>工作站</span></template>
                        <el-menu-item index="2-1">最近使用</el-menu-item>
                        <el-menu-item index="2-2">我创建的</el-menu-item>
                        <el-menu-item index="2-3">我的收藏</el-menu-item>
                        <el-menu-item index="2-4">回收站</el-menu-item>
                    </el-submenu>
                    <el-submenu index="3" style="background-color: rgb(238, 241, 246)">
                        <template slot="title"><i class="el-icon-s-claim"></i><span>团队空间</span></template>
                        <el-menu-item><el-button @click="joinTeamVisible=true">加入团队</el-button></el-menu-item>
                        <el-dialog title="加入团队" :visible.sync="joinTeamVisible" width="400px">
                        <el-form :model="join">
                            <el-form-item label="要加入的团队ID" :label-width="formLabelWidth">
                                <el-input v-model="join.team_id" autocomplete="off"></el-input>
                            </el-form-item>
                            <div>
                                <el-button @click="joinTeamVisible = false">取 消</el-button>
                                <el-button type="primary" @click="joinTeam()">确 定</el-button>
                            </div>
                        </el-form>
                        </el-dialog>
                        <el-menu-item><el-button @click="createTeamVisible=true">创建团队</el-button></el-menu-item>
                        <el-dialog title="创建团队" :visible.sync="createTeamVisible" width="400px">
                        <el-form :model="create">
                            <el-form-item label="要创建的团队名称" :label-width="formLabelWidth">
                                <el-input v-model="create.team_name" autocomplete="off"></el-input>
                            </el-form-item>
                            <div>
                                <el-button @click="createTeamVisible = false">取 消</el-button>
                                <el-button type="primary" @click="createTeam()">确 定</el-button>
                            </div>
                        </el-form>
                        </el-dialog>
                    </el-submenu>
                </el-menu>
            </el-aside>
            
            <el-main>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
import Vue from 'vue'
export default {
    data() {
        return {
            userinfo: [],
            isCollapse: false,
            joinTeamVisible:false,
            join:{
                team_id:0
            },
            createTeamVisible:false,
            create:{
                team_name:""
            }
        }
    },
    created() {
        this.getUserInfo()
    },
    methods: {
        logout() {
            window.sessionStorage.clear()
            this.$router.push('/login')
        },
        async getUserInfo() {
            const {data:res} = await this.$http.get('http://175.24.121.113:8000/myapp/user/info')
            if(res.code !== 200) return this.$message.error(res.info)
            this.userinfo = res.data
            console.log(res)
        },
        //折叠展开左菜单
        toggleCollapse() {
            this.isCollapse = !this.isCollapse
        },
        joinTeam(){
            this.joinTeamVisible=false;
            Vue.axios.get(
                "http://175.24.121.113:8000/myapp/team/join/",
                {
                    team_id:this.joinTeam.team_id
                },
                {
                    headers: {
                        token: this.$store.state.token
                    }
                }
            ).then(res=>{
                if(res.code===200){
                    alert(res.info);
                }
                else if(res.code===400){
                    alert(res.info);
                }
            }
            ).catch(res=>{
                console.log(res);
            })
        },
        createTeam(){
            this.createTeamVisible=false;
            Vue.axios.post(
                "http://175.24.121.113:8000/myapp/team/create/",
                {
                    team_name:this.createTeam.team_name
                },
                {
                    headers: {
                        token: this.$store.state.token
                    }
                }
            ).then(res=>{
                if(res.code===200){
                    alert(res.info);
                    alert("你的新团队:"+res.data.name+" id:"+res.data.id+"成功创建！");
                }
            }).catch(res=>{
                console.log(res);
            });
        }
    }
}
</script>

<style lang="less" scoped>
.el-header {
    background-color: rgb(130, 255, 213);
    color: #333;
    line-height: 60px;
    display: flex;
    justify-content: space-between;
}

.name_place {
    span {
        margin-left: 15px;
    }
}

.name {
    color: #333;
    font-size: 20px;
    display: flex;
    align-items: center;
}
  
.el-aside {
    color: #333;
}

.toggle-button {
    background-color: rgb(238, 241, 246);
    font-size: 10px;
    line-height: 24px;
    color: #333;
    text-align: center;
    letter-spacing: 0.2em;
    cursor: pointer;
}
.el-menu-item {
    background-color: rgb(238, 241, 246)
}
.a{
    text-decoration: none;
    color:#333;
}
</style>
