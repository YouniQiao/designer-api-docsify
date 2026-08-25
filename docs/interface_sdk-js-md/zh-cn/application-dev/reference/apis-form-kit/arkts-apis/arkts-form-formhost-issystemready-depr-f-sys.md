# isSystemReady（系统接口）

## 导入模块

```TypeScript
```

## isSystemReady

```TypeScript
function isSystemReady(callback: AsyncCallback<void>): void
```

检查系统是否准备好。使用callback异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [isSystemReady](arkts-form-formhost-issystemready-f-sys.md)

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**示例**

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.isSystemReady((error: Base.BusinessError) => {
  if (error.code) {
    console.error(`formHost isSystemReady, error: ${JSON.stringify(error)}`);
  }
});
```

```TypeScript
import Base from '@ohos.base';

let formId: string = '12400633174999288';
formHost.isSystemReady().then(() => {
  console.info('formHost isSystemReady success');
}).catch((error: Base.BusinessError) => {
  console.error(`formHost isSystemReady, error: ${JSON.stringify(error)}`);
});
```


## isSystemReady

```TypeScript
function isSystemReady(): Promise<void>
```

检查系统是否准备好。使用Promise异步回调。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [isSystemReady](arkts-form-formhost-issystemready-f-sys.md)

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**示例**

参见 [isSystemReady](#issystemready)
