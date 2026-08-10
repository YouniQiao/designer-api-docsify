# requestEnableLocation

## 导入模块

```TypeScript
import { geolocation } from 'kits/@kit.LocationKit';
```

## requestEnableLocation

```TypeScript
function requestEnableLocation(callback: AsyncCallback<boolean>): void
```

Request enable location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function requestEnableLocation(callback: AsyncCallback<boolean>): void--><!--Device-geolocation-function requestEnableLocation(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | Indicates the callback for reporting the location switch status. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation((err, data) => {
    if (err) {
        console.info('requestEnableLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('requestEnableLocation: data=' + JSON.stringify(data));
    }
});
```


## requestEnableLocation

```TypeScript
function requestEnableLocation(): Promise<boolean>
```

Request enable location

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

**废弃版本：** 9

**需要权限：** ohos.permission.LOCATION

<!--Device-geolocation-function requestEnableLocation(): Promise<boolean>--><!--Device-geolocation-function requestEnableLocation(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Location.Location.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | The promise returned by the function. |

## 示例

```TypeScript
import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation().then((result) => {
    console.info('promise, requestEnableLocation: ' + JSON.stringify(result));
});
```

