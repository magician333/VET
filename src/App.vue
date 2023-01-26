<script setup lang="ts">

import {
  NConfigProvider,
  NButton,
  NCard,
  NTable,
  NInput,
  NIcon,
  NEllipsis,
  NTag,
  NTimeline,
  NTimelineItem
} from 'naive-ui';

import {
  TrashOutline,
  BookmarksOutline,
  PricetagOutline,
  CalendarOutline,
  PodiumOutline,
  PlayCircleOutline,
  PauseCircleOutline,
  PlayBackCircleOutline,
  PlayForwardCircleOutline,
  DownloadOutline
} from "@vicons/ionicons5";

import { onMounted, ref } from 'vue';

let advise = ref();
let advises = new Array;
let advise_list = ref()
let time: number = 0;
let count_index: number = 1;
let video_name: string = "DEENO三维场景视频";
let video_src: string = "../video/1.mp4";
let play_status: number = 0; //0:pause 1:playing
let video_currenttime: any;
let video_duration: number;
let video_rr: string
let video_note: string
// let play_button: any = "PlayCircleOutline";

const player = ref<HTMLVideoElement>();
const v_duration = ref<HTMLDivElement>();
const v_rr = ref<HTMLDivElement>();
const v_note = ref<HTMLDivElement>();


onMounted(() => {
  player.value?.addEventListener("canplay", function () {
    v_duration.value!.textContent = "时长：" + this.duration
    v_rr.value!.textContent = "分辨率：" + this.videoWidth + "*" + this.videoHeight
    v_note.value!.textContent = "备注：" + "无"
    // video_rr = this.videoWidth + "*" + this.videoHeight
    // video_note = "无"
  }, false)
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
    var data = { "index": count_index, "time": time, "suggest": advise.value, "duration": 1 };
    advises.push(data);
    advises = advises.sort((a, b) => a.time - b.time)
    advises.forEach(i => {
      i["index"] = advises.indexOf(i) + 1
    });
    count_index++;
  }
  advise.value = "";
};

function rowclick(i: any) {
  player.value!.currentTime = i["time"];

};

function del(i: any) {
  advises.forEach(j => {
    if (i["index"] == j["index"]) {
      advises.splice(advises.indexOf(j), 1);
      advises = advises.sort((a, b) => a.time - b.time)
      advises.forEach(i => {
        i["index"] = advises.indexOf(i) + 1
      });
      count_index--;
    }
  });

  advise.value = " ";
  advise.value = "";
};

function play_video() {
  if (play_status == 0) {
    player.value?.play();
    play_status = 1;
  }
  else {
    player.value?.pause();
    play_status = 0;
  }
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
          <video :src=video_src type="video/mp4" ref="player" class="video" controls></video>
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
            <n-timeline-item type="info" v-for="i in advises" :title="'第' + i.index + '项'" :content="i.suggest"
              :time="i.time.toFixed(2) + '秒'" @click="rowclick(i)">
              <n-ellipsis style="max-width: 180px">
                {{ i["suggest"] }}
              </n-ellipsis>

              <n-button @click="del(i)" class="del_advise" text>
                <n-icon :component="TrashOutline">
                  <TrashOutline />
                </n-icon>
              </n-button>
            </n-timeline-item>
          </n-timeline>
          <n-button class="export" color="#243949" strong round>
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