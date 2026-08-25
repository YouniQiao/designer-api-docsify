# getCurrentDistrict

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## getCurrentDistrict

```TypeScript
function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>
```

获取当前设备所在区域的信息。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Location.Location.Geocoder

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [DistrictRequestParams](arkts-location-geolocationmanager-districtrequestparams-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[DistrictInfo](arkts-location-geolocationmanager-districtinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
| [3301500](../errorcode-geoLocationManager.md#3301500-区域信息包含国家码查询失败) |
