<template>
    <div height=100%>
        <span class="title">回收站</span>
        <el-divider></el-divider>
        <el-table :data="tableData" height=734px style="width: 100%" :default-sort = "{prop: 'date', order: 'descending'}">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" class="demo-table-expand">
                        <el-form-item label="最近一次修改">
                            <span>{{ props.row.modification_date }}</span>
                        </el-form-item>
                        <el-form-item label="修改人">
                            <span>{{ props.row.modifier }}</span>
                        </el-form-item>
                        <el-form-item label="修改次数">
                            <span>{{ props.row.modification_times }}</span>
                        </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column prop="date" label="创建日期" width="180"></el-table-column>
            <el-table-column prop="author" label="作者" width="180"></el-table-column>
            <el-table-column prop="name" label="文件名称" @contextmenu.prevent=""></el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-tooltip class="item" effect="dark" content="彻底删除" placement="right">
                        <el-button type="danger" icon="el-icon-delete" circle @click="handleDelete(scope.$index, scope.row)"></el-button>
                    </el-tooltip>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-03',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-04',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-05',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-06',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-07',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-08',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-09',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }, {
          date: '2016-05-10',
          author: '王小虎',
          name: '金刚石文档内容描述',
          modification_date: '2020-08-10',
          modifier: '笪昊凡',
          modification_times: '1'
        }]
      }
    }
  }
</script>

<style lang="less" scoped>
.title {
    color: #333;
    margin-bottom: -20px;
    font-size: 20px;
    line-height: 1.7;
    display: flex;
    align-items: center;
    font-family: "Microsoft YaHei", "微软雅黑", "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", Arial, sans-serif;
}
.demo-table-expand {
    font-size: 0;
}
.demo-table-expand label {
    width: 90px;
    color: #99a9bf;
}
.demo-table-expand .el-form-item {
    color: rgb(180, 180, 180);
    margin-right: 0;
    margin-bottom: 0;
    width: 20%;
}
</style>