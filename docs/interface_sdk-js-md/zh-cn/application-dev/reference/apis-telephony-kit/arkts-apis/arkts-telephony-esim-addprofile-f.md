# addProfile

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## addProfile

```TypeScript
function addProfile(profile: DownloadableProfile): Promise<boolean>
```

通过该接口拉起下载界面，允许用户添加单个配置文件。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| profile | [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3120001](../errorcode-telephony.md#3120001-服务连接失败) |
| [3120002](../errorcode-telephony.md#3120002-系统内部错误) |
