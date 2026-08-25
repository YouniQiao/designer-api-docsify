# connectToCandidateConfig

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## connectToCandidateConfig

```TypeScript
function connectToCandidateConfig(networkId: number): void
```

通过networkId连接到指定的候选热点，只允许连接自己添加的配置。此方法一次连接一个配置。 应用必须在前台运行。

**起始版本：** 12

**需要权限：** ohos.permission.SET_WIFI_INFO

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
| [2501001](../errorcode-wifi.md#2501001-sta功能未打开) |


## connectToCandidateConfig

```TypeScript
function connectToCandidateConfig(settings: ConnectSettings): Promise<void>
```

使用连接设置连接到指定的候选热点。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.SET_WIFI_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.WiFi.STA

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| settings | [ConnectSettings](arkts-connectivity-wifimanager-connectsettings-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [2501000](../errorcode-wifi.md#2501000-sta内部异常) |
| [2501001](../errorcode-wifi.md#2501001-sta功能未打开) |
| [2501005](../errorcode-wifi.md#2501005-用户未响应连接请求) |
| [2501006](../errorcode-wifi.md#2501006-用户拒绝连接请求) |
| [2501007](../errorcode-wifi.md#2501007-参数校验失败) |
