# isCellularDataEnabledSync

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## isCellularDataEnabledSync

```TypeScript
function isCellularDataEnabledSync(): boolean
```

Check whether cellular data services are enabled.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-data-function isCellularDataEnabledSync(): boolean--><!--Device-data-function isCellularDataEnabledSync(): boolean-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns { |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Internal error. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

## 示例

```TypeScript
import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataEnabledSync();
    console.info(`isCellularDataEnabledSync success : ${isEnabled}`);
} catch (err) {
    console.error(`isCellularDataEnabledSync fail. code: ${err.code}, message: ${err.message}`);  
}
```

