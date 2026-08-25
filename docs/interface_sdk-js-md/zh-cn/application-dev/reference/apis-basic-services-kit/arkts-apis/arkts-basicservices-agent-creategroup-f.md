# createGroup

## 导入模块

```TypeScript
import { request } from '@kit.BasicServicesKit';
```

## createGroup

```TypeScript
function createGroup(config: GroupConfig): Promise<string>
```

根据[GroupConfig](arkts-basicservices-agent-groupconfig-i.md)分组条件创建分组 ，并返回分组id。使用Promise异步回调。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [GroupConfig](arkts-basicservices-agent-groupconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../errorcode-request.md#13400003-服务异常) |

**示例**

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 准备分组配置选项 GroupConfig 对象。
let config: request.agent.GroupConfig = {
    notification: {},
};
// 调用 createGroup 接口创建分组。
request.agent.createGroup(config).then((gid: string) => {
  console.info(`Succeeded in creating a download task group. `);
}).catch((err: Error) => {
  console.error(`Failed to create a download group, Code: ${err.code}, message: ${err.message}`);
});
```
