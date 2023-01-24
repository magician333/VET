<script lang="ts" >
import { NConfigProvider, GlobalThemeOverrides, NButton, NCard, NTable, NInput, NIcon, NEllipsis, NTime } from 'naive-ui'
import { TrashOutline, BookmarksOutline, PricetagOutline, CalendarOutline, PodiumOutline } from "@vicons/ionicons5";
import { ref, version } from 'vue';



export default {
  data() {
    return {
      advise: "",
      advises: new Array,
      time: 0,
      index: 1,
      version: 2,
      mtime: 1674482318,
      // player: ref<HTMLVideoElement | null>(null)
    }
  },
  methods: {
    enter() {
      var comment = this.advise.trim()
      if (comment.length != 0) {
        const player = ref<HTMLVideoElement>();
        console.log(player)
        this.time = player.value?.currentTime as number
        // this.time = this.$refs["player"].currentTime
        var data = { "index": this.index, "time": this.time, "suggest": this.advise, "duration": 1 }
        this.advises.push(data)
        this.index++
      }
      this.advise = ""
    },
    rowclick(i: any) {
      let player = ref<HTMLVideoElement | null>(null)
      player.value!.currentTime = i["time"]
      // this.$refs["player"].currentTime = i["time"]
    },
    del(i: any) {
      this.advises.forEach(j => {
        if (i["time"] == j["time"]) {
          this.advises.splice(this.advises.indexOf(j), 1)
          this.index--
        }
      });
    }
  },
  components: {
    NButton,
    NCard,
    NTable,
    NInput,
    NIcon,
    TrashOutline,
    NEllipsis,
    NTime,
    BookmarksOutline,
    PricetagOutline,
    CalendarOutline,
    PodiumOutline,
  }
}
</script>

<template>
  <n-config-provider>
    <n-card class="content_area" :bordered="false">
      <div class="main_area">
        <div class="video_area">
          <div class="title_area">
            <div class="title_name">
              <h1>DEENO三维场景视频</h1>
            </div>
            <div class="title_version">
              <n-icon :component="PricetagOutline" :size="20" class="version_icon">
                <PricetagOutline />
              </n-icon>
              第{{ version }}稿
            </div>
            <div class="title_date">
              <n-icon :component="CalendarOutline" :size="20" class="date_icon">
                <CalendarOutline />
              </n-icon>
              <n-time :time="mtime" format="yyyy-MM-dd hh:mm" unix></n-time>
            </div>

          </div>
          <div ref="player"></div>
          <!-- <video src="../video/1.mp4" type="video/mp4" ref="player" controls class="video"></video> -->
          <div class="input_area">
            <n-input type="text" class="input_revise" v-model:value="advise" placeholder="请输入修改意见" round clearable>
              <template #prefix>
                <n-icon :component="BookmarksOutline">
                  <BookmarksOutline />
                </n-icon>
              </template>
              <template #suffix>
                <n-button @click="enter" class="enter" color="#5753C9" strong round>确定</n-button>
              </template>
            </n-input>
          </div>
        </div>
        <div class="advise_list">
          <div class="advise_head">
            <n-icon :component="PodiumOutline" :size="20" class="count_icon">
              <PodiumOutline />
            </n-icon>
            当前建议数量：{{ index- 1 }}
          </div>
          <n-table class="table is-hoverable" :bordered="false">
            <thead>
              <tr>
                <th class="has-text-centered">序号</th>
                <th class="has-text-centered">时间</th>
                <th class="has-text-centered">修改意见</th>
                <th class="has-text-centered">删除</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="i in advises" @click="rowclick(i)">
                <td>{{ i["index"] }}</td>
                <td>{{ i['time']}}</td>
                <td>
                  <n-ellipsis style="max-width:60px">
                    {{ i["suggest"] }}
                  </n-ellipsis>
                </td>

                <td><n-button @click="del(i)" text><n-icon :component="TrashOutline">
                      <TrashOutline />
                    </n-icon></n-button>
                </td>
              </tr>
            </tbody>

          </n-table>
        </div>
      </div>

    </n-card>
  </n-config-provider>



</template>

<style scoped>

</style>