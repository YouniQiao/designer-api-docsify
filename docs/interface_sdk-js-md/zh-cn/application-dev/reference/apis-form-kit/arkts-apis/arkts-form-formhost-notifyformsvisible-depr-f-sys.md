# notifyFormsVisible（系统接口）

## 导入模块

```TypeScript
```

## notifyFormsVisible

```TypeScript
function notifyFormsVisible(formIds: Array<string>, isVisible: boolean, callback: AsyncCallback<void>): void
```

通知卡片是否可见。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isVisible | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import Base from '@ohos.base';

let formIds: string[]= new Array('12400633174999288', '12400633174999289');
formHost.notifyFormsVisible(formIds, true, (error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost notifyFormsVisible, error: ${JSON.stringify(error)}`);
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formIds: string[] = new Array('12400633174999288', '12400633174999289');
formHost.notifyFormsVisible(formIds, true).then(() => {
  console.info('formHost notifyFormsVisible success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost notifyFormsVisible, error: ${JSON.stringify(error)}`);
});
```


## notifyFormsVisible

```TypeScript
function notifyFormsVisible(formIds: Array<string>, isVisible: boolean): Promise<void>
```

通知卡片是否可见。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md)

**需要权限：** ohos.permission.REQUIRE_FORM

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | 是 |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [notifyFormsVisible](#notifyformsvisible)
