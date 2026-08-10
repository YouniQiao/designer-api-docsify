# getCachedGnssLocationsSize

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## getCachedGnssLocationsSize

```TypeScript
function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void
```

Obtain the number of cached GNSS locations reported at a time

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCachedGnssLocationsSize

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void--><!--Device-geolocation-function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 | Indicates the callback for reporting the cached GNSS locations size. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize((err, size) => {
    if (err) {
        console.info('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
    }
    if (size) {
        console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
    }
});
```


## getCachedGnssLocationsSize

```TypeScript
function getCachedGnssLocationsSize(): Promise<number>
```

Obtain the number of cached GNSS locations reported at a time

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** ohos.geoLocationManager/geoLocationManager.getCachedGnssLocationsSize

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function getCachedGnssLocationsSize(): Promise<number>--><!--Device-geolocation-function getCachedGnssLocationsSize(): Promise<number>-End-->

**系统能力：** SystemCapability.Location.Location.Gnss

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;number&gt; | The promise returned by the function. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize().then((result) => {
    console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
});
```

