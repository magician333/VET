<script setup lang="ts">
import { NConfigProvider, NButton, NCard, NTable, NInput, NIcon, NEllipsis, NTime } from 'naive-ui'
import { TrashOutline, BookmarksOutline, PricetagOutline, CalendarOutline, PodiumOutline } from "@vicons/ionicons5";
import { ref } from 'vue';

let advise = ref();
let advises = new Array;
let advise_list = ref()
let time: number = 0;
let index: number = 1;
let version: number = 2;
let mtime: number = 1674482318;
let video_name: string = "DEENO三维场景视频";

const player = ref<HTMLVideoElement>();
const themeOverrides = {
  common: {
    primaryColor: "#6E7FF3",
    primaryColorHover: "#6E7FF3"
  },
}

function enter() {
  if (advise.value.length != 0) {
    time = player.value?.currentTime as number;
    var data = { "index": index, "time": time, "suggest": advise.value, "duration": 1 };
    advises.push(data);
    index++;
  }
  advise.value = "";
};

function rowclick(i: any) {
  player.value!.currentTime = i["time"];

};

function del(i: any) {
  advises.forEach(j => {
    if (i["time"] == j["time"]) {
      advises.splice(advises.indexOf(j), 1);
      index--;
    }
  });

  advise.value = "111111"
  advise.value = ""
};


</script>

<template>
  <n-config-provider :theme-overrides="themeOverrides">

    <n-card class="content_area" :bordered="false">
      <div class="main_area">
        <div class="video_area">
          <div class="title_area">
            <div class="title_name">
              {{ video_name }}
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
          <video src="../video/1.mp4" type="video/mp4" ref="player" controls class="video"></video>
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
              <tr v-for="i in advises" @click="rowclick(i)" ref="advise_list">
                <td>{{ i["index"] }}</td>
                <td>{{ i['time'].toFixed(2) }}</td>
                <td>
                  <n-ellipsis style="max-width:60px">
                    {{ i["suggest"] }}
                  </n-ellipsis>
                </td>
                <td>
                  <n-button @click="del(i)" text>
                    <n-icon :component="TrashOutline">
                      <TrashOutline />
                    </n-icon>
                  </n-button>
                </td>
              </tr>
            </tbody>

          </n-table>
        </div>
      </div>

    </n-card>
  </n-config-provider>
</template>