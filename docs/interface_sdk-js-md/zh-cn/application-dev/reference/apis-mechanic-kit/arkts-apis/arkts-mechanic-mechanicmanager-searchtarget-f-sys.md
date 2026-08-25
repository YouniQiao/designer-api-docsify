# searchTarget（系统接口）

## 导入模块

```TypeScript
import { mechanicManager } from 'kits/@kit.MechanicKit';
```

## searchTarget

```TypeScript
function searchTarget(target: TargetInfo, params: SearchParams): Promise<SearchResult>
```

Searching for a specified target.

**起始版本：** 21

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [TargetInfo](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-targetinfo-i.md) | 是 |
| params | [SearchParams](../../apis-arkui/arkts-apis/arkts-arkui-atomicservice-atomicservicesearch-searchparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SearchResult & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |
| [33300003](../errorcode-mechanic.md#33300003-功能不支持) |
| 33300004 |
