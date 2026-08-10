# removeFusionFence（系统接口）

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## removeFusionFence

```TypeScript
function removeFusionFence(identifier: string): Promise<void>
```

Remove a fusion fence.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>--><!--Device-geoLocationManager-function removeFusionFence(identifier: string): Promise<void>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| identifier | string | 是 | Indicates identifier of the fusion fence. The string format should be a valid unique identifier (e.g., GUID or specific alphanumeric pattern). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 3301602 | Failed to delete a fusion fence due to an incorrect identifier. |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.removeFusionFence} due to limited device. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

try {
  // 必须与addFusionFence传入的identifier相同才能成功删除围栏
  let identifier = "123456789";
  await geoLocationManager.removeFusionFence(identifier).then(() => {
    // 围栏删除成功
    console.info("removeFusionFence success");
  }).catch((error : BusinessError) => {
    console.error("removeFusionFence: BusinessError=" + JSON.stringify(error));
  });
} catch(error) {
  console.error("removeFusionFence: error=" + JSON.stringify(error));
}
```

