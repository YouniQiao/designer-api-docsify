# addContactViaUI

## 导入模块

```TypeScript
```

## addContactViaUI

```TypeScript
function addContactViaUI(context: Context, contact: Contact): Promise<number>
```

调用新建联系人接口，打开新建联系人UI界面。使用Promise异步回调。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

<!--Device-contact-function addContactViaUI(context: Context, contact: Contact): Promise<number>--><!--Device-contact-function addContactViaUI(context: Context, contact: Contact): Promise<number>-End-->

**系统能力：** SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16700102](../errorcode-contacts.md#16700102-增删改数据库失败) |
| [16700103](../errorcode-contacts.md#16700103-用户取消) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |

**示例**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// 请在组件内获取context。
let contactInfo: contact.Contact = {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.addContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(`Succeeded in add Contact via UI.data->${JSON.stringify(data)}`);
  });
```
