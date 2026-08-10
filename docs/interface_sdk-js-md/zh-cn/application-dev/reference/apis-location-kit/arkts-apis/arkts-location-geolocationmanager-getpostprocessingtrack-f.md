# getPostProcessingTrack

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getPostProcessingTrack

```TypeScript
function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>
```

Obtain post-processing trajectory information under specific sport mode. Only  
[SKIING](arkts-location-geolocationmanager-sportstype-e.md#skiing) is supported currently.

Before calling this API, you need to call  
[on('locationChange')](geoLocationManager.on('locationChange')) and set the input parameter  
[sportsType](arkts-location-geolocationmanager-continuouslocationrequest-i.md#sportstype) to the specific sport mode to start tracking.

Returns data within 24 hours since tracking started; Subsequent calls return only new records.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**需要权限：** ohos.permission.LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>--><!--Device-geoLocationManager-function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sportsType | [SportsType](arkts-location-geolocationmanager-sportstype-e.md) | 是 | Indicate the type of sports. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;Location&gt;&gt; | Promise used to return `Array&lt;Location&gt;`. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.getPostProcessingTrack} due to limited device capabilities. |
| 3301200 | Failed to obtain the post processing track because sports type is not supported. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let request: geoLocationManager.ContinuousLocationRequest = {
  'interval': 1,
  'locationScenario': geoLocationManager.UserActivityScenario.SPORT,
  // 设置运动类型为滑雪
  'sportsType': geoLocationManager.SportsType.SKIING,
};

let locationCallback = (location: geoLocationManager.Location): void => {
  console.info('locationCallback: data: ' + JSON.stringify(location));
};

let processTrackTask = (): void => {
  // 先移除定位请求
  geoLocationManager.off('locationChange', locationCallback);
  // 获取后处理轨迹
  geoLocationManager.getPostProcessingTrack(geoLocationManager.SportsType.SKIING)
    .then((res) => {
      console.info('getPostProcessingTrack len: ' + JSON.stringify(res.length));
    }).catch((err: BusinessError) => {
      console.info('getPostProcessingTrack err: ' + JSON.stringify(err));
    })
}

try {
  // 发起滑雪模式定位请求
  geoLocationManager.on('locationChange', request, locationCallback);
  // 满足轨迹采集条件后，移除定位请求并获取后处理轨迹，这里设定30分钟后满足轨迹采集要求。
  let delayTaskTime = 30 * 60 * 1000;
  setTimeout(processTrackTask, delayTaskTime);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

