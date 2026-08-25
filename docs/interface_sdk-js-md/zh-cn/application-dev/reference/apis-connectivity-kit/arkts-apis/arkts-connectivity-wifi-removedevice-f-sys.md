# removeDevice（系统接口）

## 导入模块

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## removeDevice

```TypeScript
function removeDevice(id: number): boolean
```

移除指定的网络配置。<p>删除WLAN网络后，其配置将从网络配置列表中删除。 如果正在连接该WLAN网络，连接将被中断。 应用只能删除自己创建的WLAN网络。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** removeDeviceConfig

**需要权限：** ohos.permission.SET_WIFI_INFO and ohos.permission.MANAGE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import wifi from '@ohos.wifi';

try {
    let id = 0;
    wifi.removeDevice(id);        
}catch(error){
    console.error("failed:" + JSON.stringify(error));
}
```
