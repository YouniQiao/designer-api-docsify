# getAllFormsInfo（系统接口）

## 导入模块

```TypeScript
```

## getAllFormsInfo

```TypeScript
function getAllFormsInfo(callback: AsyncCallback<Array<formInfo.FormInfo>>): void
```

获取设备上所有应用提供的卡片信息。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.FormInfo&gt;&gt; | 是 |

**示例**

```TypeScript
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

formHost.getAllFormsInfo((error: Base.BusinessError, data: formInfo.FormInfo[]) => {
  if (error.code) {
    console.error(`formHost getAllFormsInfo, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`formHost getAllFormsInfo, data: ${JSON.stringify(data)}`);
  }
});
```

```TypeScript
import formInfo from '@ohos.app.form.formInfo';
import Base from '@ohos.base';

formHost.getAllFormsInfo().then((data: formInfo.FormInfo[]) => {
  console.info(`formHost getAllFormsInfo data: ${JSON.stringify(data)}`);
}).catch((error: Base.BusinessError) => {
  console.error(`formHost getAllFormsInfo, error: ${JSON.stringify(error)}`);
});
```


## getAllFormsInfo

```TypeScript
function getAllFormsInfo(): Promise<Array<formInfo.FormInfo>>
```

获取设备上所有应用提供的卡片信息。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md)

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;formInfo.FormInfo & gt; & gt; |

**示例**

参见 [getAllFormsInfo](#getallformsinfo)
