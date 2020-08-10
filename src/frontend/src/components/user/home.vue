<template>
    <el-container style="height: 100%; border: 1px solid #eee">
        <el-header style="text-align: right; font-size: 12px">
            <el-dropdown>
                <i class="el-icon-setting" style="margin-right: 15px"></i>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>退出登录</el-dropdown-item>
                    <el-dropdown-item>注销账号</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
            <span>昵称</span>
        </el-header>
        
        <el-container>
            <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
                <el-menu :default-openeds="['1', '3']">
                    <el-submenu index="1">
                        <template slot="title"><i class="el-icon-user-solid"></i>个人空间</template>
                        <el-menu-item-group>
                            <template slot="title">个人信息</template>
                            <el-menu-item index="1-1">个人详情</el-menu-item>
                            <el-menu-item index="1-2">消息通知</el-menu-item>
                        </el-menu-item-group>
                        <el-menu-item-group title="账号与安全">
                            <el-menu-item index="1-3">修改个人信息</el-menu-item>
                            <el-menu-item index="1-4">修改密码</el-menu-item>
                        </el-menu-item-group>
                    </el-submenu>
                    <el-submenu index="2">
                        <template slot="title"><i class="el-icon-menu"></i>工作站</template>
                        <el-menu-item index="2-1">最近使用</el-menu-item>
                        <el-menu-item index="2-2">我创建的</el-menu-item>
                        <el-menu-item index="2-3">我的收藏</el-menu-item>
                        <el-menu-item index="2-4">回收站</el-menu-item>
                    </el-submenu>
                    <el-submenu index="3">
                        <template slot="title"><i class="el-icon-s-claim"></i>团队空间</template>
                    </el-submenu>
                </el-menu>
            </el-aside>
  
            <el-main>
      
            </el-main>
        </el-container>
    </el-container>
</template>

<script>

</script>

<style>
.el-header {
    background-color: rgb(130, 255, 213);
    color: #333;
    line-height: 60px;
}
  
.el-aside {
    color: #333;
}
</style>
