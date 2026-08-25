# isCleartextPermittedByHostName

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## isCleartextPermittedByHostName

```TypeScript
export function isCleartextPermittedByHostName(hostName: string): boolean
```

从应用预置network_config.json文件中获取按域名明文HTTP是否允许信息，默认允许明文HTTP访问。

**起始版本：** 18

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hostName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
