# removeGnssGeofence

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeGnssGeofence

```TypeScript
function removeGnssGeofence(geofenceId: int): Promise<void>
```

Remove a geofence.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本12 - 24：ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

<!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>--><!--Device-geoLocationManager-function removeGnssGeofence(geofenceId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| geofenceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the ID of geofence. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 3301602 | Failed to delete a geofence due to an incorrect ID. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.removeGnssGeofence} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API.<br>**适用版本：** 12 - 24 |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';
// fenceId是在geoLocationManager.addGnssGeofence执行成功后获取的
let fenceId = 1;
try {
  if (geoLocationManager.isGnssFenceServiceSupported()) {
    geoLocationManager.removeGnssGeofence(fenceId).then(() => {
      console.info("removeGnssGeofence success fenceId:" + fenceId);
    }).catch((error: BusinessError) => {
      console.error("removeGnssGeofence: error=" + JSON.stringify(error));
    });
  }
} catch (error) {
  console.error("removeGnssGeofence: error=" + JSON.stringify(error));
}
```

