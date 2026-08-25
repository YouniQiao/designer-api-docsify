# getFormIdsByFormLocation（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## getFormIdsByFormLocation

```TypeScript
function getFormIdsByFormLocation(location: formInfo.FormLocation): Promise<Array<string>>
```

获取设备上指定卡片位置的卡片标识列表。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| location | formInfo.FormLocation | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16501016](../errorcode-form.md#16501016-卡片位置信息无效) |
