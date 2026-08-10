# isCleartextPermittedByHostName

## 导入模块

```TypeScript
import { networkSecurity } from 'kits/@kit.NetworkKit';
```

## isCleartextPermittedByHostName

```TypeScript
export function isCleartextPermittedByHostName(hostName: string): boolean
```

Checks whether the Cleartext traffic for a specified hostname is permitted.To invoke this method, you must have the {@code ohos.permission.INTERNET} permission.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.INTERNET

<!--Device-networkSecurity-export function isCleartextPermittedByHostName(hostName: string): boolean--><!--Device-networkSecurity-export function isCleartextPermittedByHostName(hostName: string): boolean-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | Indicates the host name. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Returns true if the Cleartext traffic is permitted, else returns false. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

## 示例

```TypeScript
import { networkSecurity } from '@kit.NetworkKit';

try {
  let result: boolean = networkSecurity.isCleartextPermittedByHostName("xxx");
  console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
} catch (error) {
  console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
}
```

