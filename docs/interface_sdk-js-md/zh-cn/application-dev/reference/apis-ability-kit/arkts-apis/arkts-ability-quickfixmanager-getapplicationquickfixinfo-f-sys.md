# getApplicationQuickFixInfo（系统接口）

## getApplicationQuickFixInfo

```TypeScript
function getApplicationQuickFixInfo(bundleName: string, callback: AsyncCallback<ApplicationQuickFixInfo>): void
```

获取应用的快速修复信息。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-quickFixManager-function getApplicationQuickFixInfo(bundleName: string, callback: AsyncCallback<ApplicationQuickFixInfo>): void--><!--Device-quickFixManager-function getApplicationQuickFixInfo(bundleName: string, callback: AsyncCallback<ApplicationQuickFixInfo>): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationQuickFixInfo](arkts-ability-quickfixmanager-applicationquickfixinfo-i-sys.md)&gt; | 是 | 回调函数。返回应用的快速修复信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [18500008](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#18500008-快速修复内部错误) | Internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not system application. |
| [18500001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#18500001-指定的包名无效) | The bundle does not exist or no patch has been applied. |

## 示例

```TypeScript
import { quickFixManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = 'bundleName';
  quickFixManager.getApplicationQuickFixInfo(bundleName, (error, data) => {
    if (error) {
      console.error(`getApplicationQuickFixInfo error: ${error}`);
    } else {
      console.info(`getApplicationQuickFixInfo success: ${data}`);
    }
  });
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```


## getApplicationQuickFixInfo

```TypeScript
function getApplicationQuickFixInfo(bundleName: string): Promise<ApplicationQuickFixInfo>
```

获取应用的快速修复信息。使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-quickFixManager-function getApplicationQuickFixInfo(bundleName: string): Promise<ApplicationQuickFixInfo>--><!--Device-quickFixManager-function getApplicationQuickFixInfo(bundleName: string): Promise<ApplicationQuickFixInfo>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.QuickFix

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用Bundle名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[ApplicationQuickFixInfo](arkts-ability-quickfixmanager-applicationquickfixinfo-i-sys.md)&gt; | Promise对象。返回应用的快速修复信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [18500008](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#18500008-快速修复内部错误) | Internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not system application. |
| [18500001](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-ability-kit/errorcode-ability.md#18500001-指定的包名无效) | The bundle does not exist or no patch has been applied. |

## 示例

```TypeScript
import { quickFixManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = 'bundleName';
  quickFixManager.getApplicationQuickFixInfo(bundleName).then((data) => {
    console.info(`getApplicationQuickFixInfo success: ${data}`);
  }).catch((error: BusinessError) => {
    console.error(`getApplicationQuickFixInfo err: ${error}`);
  });
} catch (paramError) {
  console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
}
```

