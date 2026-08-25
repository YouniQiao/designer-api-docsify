# closeFormEditAbility

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## closeFormEditAbility

```TypeScript
function closeFormEditAbility(isMainPage?: boolean): void
```

关闭卡片编辑页。适用于卡片编辑完成或取消编辑的场景，例如用户完成参数配置后关闭编辑页、取消编辑操作等。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isMainPage | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16501015](../errorcode-form.md#16501015-不能关闭其他应用的半模态卡片编辑页) |
