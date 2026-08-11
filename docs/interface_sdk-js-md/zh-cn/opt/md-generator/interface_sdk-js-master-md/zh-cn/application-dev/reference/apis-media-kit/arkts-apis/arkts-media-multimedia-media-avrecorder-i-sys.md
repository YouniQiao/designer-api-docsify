# AVRecorder

音视频录制管理类，用于音视频媒体录制。在调用AVRecorder的方法前，需要先调用  
[createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder)接口构建一个AVRecorder实例。

音视频录制demo可参考：[音频录制开发指导](../../../media/media/using-avrecorder-for-recording.md)、  
[视频录制开发指导](../../../media/media/video-recording.md)。

> **说明：**
> 
> - 本Interface首批API从API version 9开始支持。
> 
> - 相机视频录制功能需配合相机模块使用，相机模块接口的使用详情请参考[相机管理](../../apis-camera-kit/arkts-apis/arkts-multimedia-camera.md/arkts-multimedia-camera.md)。

**起始版本：** 9

<!--Device-unnamed-interface AVRecorder--><!--Device-unnamed-interface AVRecorder-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

## getInputMetaSurface

```TypeScript
getInputMetaSurface(type: MetaSourceType): Promise<string>
```

获取指定元数据源类型的输入元数据surface。必须在prepare完成后和start之前调用。

**起始版本：** 12

<!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string>--><!--Device-AVRecorder-getInputMetaSurface(type: MetaSourceType): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [MetaSourceType](arkts-media-multimedia-media-metasourcetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;string&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../errorcode-media.md#5400103-出现io错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [5400105](../errorcode-media.md#5400105-播放服务死亡) |

## isWatermarkSupported

```TypeScript
isWatermarkSupported(): Promise<boolean>
```

查询设备是否支持硬件数字水印。使用Promise异步回调。

可以在prepare()、start()或pause()事件触发后调用。

**起始版本：** 13

<!--Device-AVRecorder-isWatermarkSupported(): Promise<boolean>--><!--Device-AVRecorder-isWatermarkSupported(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

avRecorder.isWatermarkSupported().then((isWatermarkSupported: boolean) => {
  console.info(`Succeeded in get, isWatermarkSupported: ${isWatermarkSupported}`);
}).catch((error: BusinessError) => {
  console.error(`Failed to get and catch error is ${error.message}`);
});
```

## setWatermark

```TypeScript
setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>
```

为AVRecorder设置水印。使用Promise异步回调。

只能在prepare()事件触发后且start()事件触发前调用。

**起始版本：** 13

<!--Device-AVRecorder-setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>--><!--Device-AVRecorder-setWatermark(watermark: image.PixelMap, config: WatermarkConfig): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watermark | image.PixelMap | 是 |
| config | [WatermarkConfig](arkts-media-multimedia-media-watermarkconfig-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let watermark: image.PixelMap|undefined = undefined; // need data.
let watermarkConfig: media.WatermarkConfig = { top: 100, left: 100 }

avRecorder.setWatermark(watermark, watermarkConfig).then(() => {
  console.info('Succeeded in setWatermark');
}).catch((error: BusinessError) => {
  console.error(`Failed to setWatermark and catch error is ${error.message}`);
});
```
