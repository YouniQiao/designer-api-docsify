# @ohos.multimedia.avInputCastPicker(录音设备选择组件)

本模块提供创建录音设备选择组件AVInputCastPicker的功能，提供录音设备发现与连接的统一入口。

> **说明：**
 >
 > - 示例效果请以真机为准，当前DevEco Studio预览器无实际录音设备选择功能。<!--Del-->
 >
 > - 当前组件的使用，依赖于设备支持“录音设备选择界面”。当前暂无OpenHarmony设备支持，需要OEM厂商实现具体的“录音设备选择界面”。
 >
 > - API版本26.0.0之前，此组件仅支持在PC/2in1上使用；API版本26.0.0及之后，此组件新增支持在手机、平板上使用。<!--DelEnd-->

## 属性

支持[通用属性](../../apis-arkui/arkts-components/arkts-arkui-common-comp.md)。

## 事件

支持[通用事件](../../apis-arkui/arkts-components/arkts-arkui-common-comp.md)。

## 导入模块

```TypeScript
import { AVInputCastPicker } from '@kit.AVSessionKit';
```

## 汇总

### 结构体

| 名称 | 说明 |
| --- | --- |
| [AVInputCastPicker](arkts-avsession-multimedia-avinputcastpicker-avinputcastpicker-s.md) | 录音设备选择组件，可用于切换音频输入设备。 |

### 类型

| 名称 | 说明 |
| --- | --- |
| [OnPickerStateCallback](arkts-avsession-onpickerstatecallback-t.md) |  |

## 示例

录音设备选择组件功能的示例说明参考如下。

```TypeScript
import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {

  @State pickerImage: ResourceStr = $r('app.media.layered_image'); // 自定义资源。

  private onStateChange(state: AVCastPickerState) {
    if (state == AVCastPickerState.STATE_APPEARING) {
      console.info('The picker starts showing.');
    } else if (state == AVCastPickerState.STATE_DISAPPEARING) {
      console.info('The picker finishes presenting.');
    }
  }

  @Builder
  customPickerBuilder() {
    Image(this.pickerImage)
      .width('100%')
      .height('100%')
      .fillColor(Color.Black)
  }

  build() {
    Row() {
      Column() {
        AVInputCastPicker({
          customPicker: () => this.customPickerBuilder(),
          onStateChange: this.onStateChange
        })
          .width('40vp')
          .height('40vp')
          .border({ width: 1, color: Color.Red })
      }.height('50%')
    }.width('50%')
  }
}
```
