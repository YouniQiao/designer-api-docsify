# getLastLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getLastLocation

```TypeScript
function getLastLocation(callback: AsyncCallback<Location>): void
```

Obtain last known location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getLastLocation

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getLastLocation(callback: AsyncCallback<Location>): void--><!--Device-geolocation-function getLastLocation(callback: AsyncCallback<Location>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Location&gt; | 是 | Indicates the callback for reporting the location result. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation((err, data) => {
    if (err) {
        console.info('getLastLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getLastLocation: data=' + JSON.stringify(data));
    }
});
```


## getLastLocation

```TypeScript
function getLastLocation(): Promise<Location>
```

Obtain last known location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getLastLocation

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getLastLocation(): Promise<Location>--><!--Device-geolocation-function getLastLocation(): Promise<Location>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Location&gt; | The promise returned by the function. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getLastLocation().then((result) => {
    console.info('getLastLocation: result: ' + JSON.stringify(result));
});
```

