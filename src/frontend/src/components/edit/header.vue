<template>
    <el-row type="flex" class="row-bg">
        <!-- 居中 -->
        <el-col :span="3"><div class="grid-content bg-purple">金刚石文档</div></el-col>
        <el-col :span="4">
            <div class="grid-content bg-purple">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item>工作台</el-breadcrumb-item>
                    <el-breadcrumb-item>文档编辑</el-breadcrumb-item>
                </el-breadcrumb>
            </div>
        </el-col>
        <el-col :span="1">
          <div class="grid-content bg-purple">
             <el-tooltip class="item" effect="light" content="用户收藏" placement="bottom">
              <i v-if="show_collect" class="el-icon-star-on" @click="Collect"></i>
              <i v-else class="el-icon-star-off" @click="Collect"></i>
             </el-tooltip>
          </div>
        </el-col>
        <el-col :span="13"></el-col>
        <el-col :span="2" v-color:><div class="grid-content2 bg-purple">正在编辑</div></el-col>
        <el-col :span="2">
          <div class="grid-content bg-purple">
          <el-dropdown>
            <el-avatar> user </el-avatar>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item>信息修改</el-dropdown-item>
                <el-dropdown-item>退出登录</el-dropdown-item>
              </el-dropdown-menu>
          </el-dropdown>
          </div>
        </el-col>
    </el-row>
</template>

<script>
  export default {
    data() {
      return {
        show_collect: true,
      };
    },
    watch:{
    },
    methods: {
      Collect() {
        if(this.show_collect == true)
            this.show_collect=false;
        else    
            this.show_collect=true;
      }
    }
  }
</script>

<style scoped>
    .el-row {
        margin-bottom: 15px;
    }
    .el-col {
    border-radius: 4px;
    }
  .bg-purple {
    background: #e7eff8;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    font-size: 15px;
    display:flex;
    justify-content:center;
    align-items:center;
  }
  .grid-content2{
    border-radius: 4px;
    min-height: 36px;
    font-size: 15px;
    display:flex;
    justify-content:center;
    align-items:center;
    color: #409EFF;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #e7eff8;
  }

</style>
