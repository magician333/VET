<script setup lang="ts">

import {
  NConfigProvider,
  NButton,
  NInput,
  NIcon,
  NEllipsis,
  NTimeline,
  NTimelineItem
} from 'naive-ui';

import {
  TrashOutline,
  BookmarksOutline,
  PodiumOutline,
  DownloadOutline
} from "@vicons/ionicons5";

import { onMounted, ref } from 'vue';
import axios from "axios";

let advise = ref();
let advises = new Array;
let time: number = 0;
let count_index: number = 1;
let video_name: string = "Video Name";
let video_src: string = "#";
let play_status: number = 0; //0:pause 1:playing

const url: string = "http://localhost:8080/"
const player = ref<HTMLVideoElement>();
const v_duration = ref<HTMLDivElement>();
const v_rr = ref<HTMLDivElement>();
const v_note = ref<HTMLDivElement>();


onMounted(() => {
  player.value?.addEventListener("canplay", function () {
    v_duration.value!.textContent = "时长：" + this.duration;
    v_rr.value!.textContent = "分辨率：" + this.videoWidth + "*" + this.videoHeight;
    v_note.value!.textContent = "备注：" + "无";
  }, false);

  axios.get(url + "get_video").then((res: any) => {
    video_src = url + res.data["video_src"]
    video_name = res.data["video_name"]
    advise.value = " "
    advise.value = ""
  });

  axios.get(url).then((res: any) => {
    console.log(res.data);
    (res.data).forEach((data: any) => {
      advises.push(data);
      count_index++
    });
    advise.value = " ";
    advise.value = "";
  });


})

const themeOverrides = {
  common: {
    primaryColor: "#517fa4",
    primaryColorHover: "#517fa4"
  },
}

function enter() {
  if (advise.value.length != 0) {
    time = player.value?.currentTime as number;
    advises.forEach(i => {
      if (i["time"] == time) {
        advises.splice(advises.indexOf(i), 1);

        advises.forEach(i => {
          i["index"] = advises.indexOf(i) + 1
        });
        count_index--;
      }
    });

    var data = { "index": count_index, "time": time, "advise": advise.value };
    advises.push(data);
    axios.post(url + "add_data", {
      "data": data
    }).then((res: any) => {
      console.log(res.data)
    })
    advises = advises.sort((a, b) => a.time - b.time);
    advises.forEach(i => {
      i["index"] = advises.indexOf(i) + 1
    });
    count_index++;
  }
  advises = advises.sort((a, b) => a.time - b.time);
  advise.value = "";
};

function rowclick(i: any) {
  player.value!.currentTime = i["time"];
  advise.value = i["advise"];
};

function del(i: any) {
  advises.forEach(j => {
    if (i["index"] == j["index"]) {
      advises.splice(advises.indexOf(j), 1);
      advises.forEach(i => {
        i["index"] = advises.indexOf(i) + 1;
      });
    }
  });
  //测试删除后重新添加排序是否正确
  axios.post(url + "del_data", {
    "del_index": i["index"]
  }).then((res: any) => {
    console.log(res)
  });
  advises = advises.sort((a, b) => a.time - b.time);
  count_index--;
  advise.value = " ";
  advise.value = "";
};

function videotimeupdate() {
  player.value?.addEventListener("timeupdate", function () {
    advises.forEach(i => {
      if (i["time"] == this.currentTime) {
        advise.value = i["advise"];
      }
    });

  })
}

function export_data() {
  alert("功能暂未开放");
}
</script>

<template>
  <n-config-provider :theme-overrides="themeOverrides">

    <div class="content_area">
      <div class="main_area">
        <div class="video_area">

          <div class="title_area">
            <div class="title_name">
              {{ video_name }}
            </div>
            <div class="video_info" size="small">
              <div class="v_duration" ref="v_duration"></div>
              <div class="v_rr" ref="v_rr"></div>
              <div class="v_note" ref="v_note"></div>
            </div>
          </div>

          <video :src=video_src type="video/mp4" ref="player" class="video" @timeupdate="videotimeupdate" controls>
            <canvas class="mark" ref="mark"></canvas>
          </video>
          <div class="input_area">
            <n-input type="text" class="input_revise" v-model:value="advise" placeholder="请输入修改意见" round clearable>
              <template #prefix>
                <n-icon :component="BookmarksOutline">
                  <BookmarksOutline />
                </n-icon>
              </template>
            </n-input>
            <n-button @click="enter" class="enter" color="#243949" strong round>确定</n-button>
          </div>
        </div>

        <div class="advise_list">
          <div class="advise_head">
            <n-icon :component="PodiumOutline" :size="20" class="count_icon">
              <PodiumOutline />
            </n-icon>
            当前内容数量：{{ count_index- 1 }}
          </div>
          <n-timeline class="timeline">
            <n-timeline-item type="info" v-for="i in advises" :title="'第' + i.index + '项'" :content="i.advise"
              :time="i.time.toFixed(2) + '秒'" @click="rowclick(i)">
              <n-ellipsis style="max-width: 180px">
                {{ i["advise"] }}
              </n-ellipsis>

              <n-button @click="del(i)" class="del_advise" text>
                <n-icon :component="TrashOutline">
                  <TrashOutline />
                </n-icon>
              </n-button>
            </n-timeline-item>
          </n-timeline>
          <n-button class="export" color="#243949" @click="export_data" strong round>
            <n-icon :component="DownloadOutline" style="margin-right: 5px;">
              <DownloadOutline />
            </n-icon>
            导出数据
          </n-button>
        </div>
      </div>
    </div>
  </n-config-provider>
</template>