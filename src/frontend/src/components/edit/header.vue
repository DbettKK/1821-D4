<template>
    <el-row type="flex" class="row-bg">
        <!-- 居中 -->
        <el-col :span="3"><div class="grid-content bg-purple">金刚石文档</div></el-col>
        <el-col :span="4">
            <div class="grid-content bg-purple">
                <el-breadcrumb separator="/">
                    <el-breadcrumb-item>首页</el-breadcrumb-item>
                    <el-breadcrumb-item><a href="/recently">工作台</a></el-breadcrumb-item>
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
        <el-col :span="11"></el-col>
        <el-col :span="1">
          <el-tooltip class="item" effect="light" content="添加到团队中" placement="bottom-end">
            <el-button class="share-button" icon="el-icon-folder-add" type="primary" @click="Add_G"></el-button>
          </el-tooltip>
        </el-col>
        <el-col :span="1">
          <el-button class="share-button" icon="el-icon-share" type="primary" @click="dialogVisible = true"></el-button>
          <el-dialog
            title=文档分享
            :visible.sync="dialogVisible"
            width="30%"
            :before-close="handleClose">
            <span>您的文档邀请码url为：{{url}}</span>
            <span slot="footer" class="dialog-footer">
              <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
          </el-dialog>
        </el-col>
        <el-col :span="2" v-color:><div class="grid-content2 bg-purple">正在编辑</div></el-col>
        <el-col :span="2">
          <div class="grid-content bg-purple">
          <el-dropdown>
            <el-avatar> user </el-avatar>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item><router-link to="/changeinfo" class="a">信息修改</router-link></el-dropdown-item>
                <el-dropdown-item><div @click="exit">退出登录</div></el-dropdown-item>
              </el-dropdown-menu>
          </el-dropdown>
          </div>
        </el-col>
    </el-row>
    
</template>

<script>
  import Vue from 'vue'
  export default {
    props:{
        url:{
          type:String,
        }
    },
    data() {
      return {
        show_collect: true,
        dialogVisible:false,
      };
    },
    created:function(){
        this.Get_file();
    },
    watch:{
    },
    methods: {
      Collect() {
        if(this.show_collect == true)
            this.show_collect=false;
        else    
            this.show_collect=true;
      },
      ToInfo(){
        this.$router.push(
            '/changeInfo'
        );
      },
      Add_G(){

      },
      exit(){
        window.sessionStorage.clear()
        this.$router.push('/login')
      },
      C_file(){
            Vue.axios.get(
                'http://175.24.121.113:8000/myapp/file/favorite',
                {
                  file_id:this.url
                },
                {
                headers:{
                    token:this.token
                    }
                }
            ).then(res=>{
                console.log(res.data);
            }).catch(function(error){
                console.log(error);
            })
      },
      Q_file(){
        Vue.axios.get(
                'http://175.24.121.113:8000/myapp/file/cancelfavor',
                {
                  file_id:this.url
                },
                {
                headers:{
                    token:this.token
                    }
                }
            ).then(res=>{
                console.log(res.data);
            }).catch(function(error){
                console.log(error);
            })
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
  .a{
    text-decoration: none;
    color:#333;
}
</style>
