<template>
    <el-container style="height: 100%; border: 1px solid #eee">
        <el-header style="text-align: right; font-size: 12px">
            <div class="name_place">
                <span class="name">金刚石文档</span>
            </div>
            <div>
                <el-dropdown>
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item @click.native="logout">退出登录</el-dropdown-item>
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
                        <el-menu-item-group title="账号与安全" style="background-color: rgb(238, 241, 246)">
                            <el-menu-item index="1-3">修改个人信息</el-menu-item>
                            <el-menu-item index="1-4">修改密码</el-menu-item>
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
export default {
    data() {
        return {
            userinfo: [],
            isCollapse: false
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
</style>
