# setWifiProfile

## setWifiProfile

```TypeScript
function setWifiProfile(admin: Want, profile: WifiProfile, callback: AsyncCallback<void>): void
```

为当前设备配置Wi-Fi，使连接到指定网络。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [wifiManager.setWifiProfileSync](arkts-mdm-wifimanager-setwifiprofilesync-f.md#setwifiprofilesync)

**需要权限：** ohos.permission.ENTERPRISE_SET_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-wifiManager-function setWifiProfile(admin: Want, profile: WifiProfile, callback: AsyncCallback<void>): void--><!--Device-wifiManager-function setWifiProfile(admin: Want, profile: WifiProfile, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| profile | [WifiProfile](arkts-mdm-wifimanager-wifiprofile-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'name',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
};

wifiManager.setWifiProfile(wantTemp, profile, (err) => {
  if (err) {
    console.error(`Failed to set wifi profile. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting wifi profile');
});
```


## setWifiProfile

```TypeScript
function setWifiProfile(admin: Want, profile: WifiProfile): Promise<void>
```

为当前设备配置Wi-Fi，使连接到指定网络。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** [wifiManager.setWifiProfileSync](arkts-mdm-wifimanager-setwifiprofilesync-f.md#setwifiprofilesync)

**需要权限：** ohos.permission.ENTERPRISE_SET_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-wifiManager-function setWifiProfile(admin: Want, profile: WifiProfile): Promise<void>--><!--Device-wifiManager-function setWifiProfile(admin: Want, profile: WifiProfile): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| profile | [WifiProfile](arkts-mdm-wifimanager-wifiprofile-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let profile: wifiManager.WifiProfile = {
  // 需根据实际情况进行替换
  'ssid': 'name',
  'preSharedKey': 'passwd',
  'securityType': wifiManager.WifiSecurityType.WIFI_SEC_TYPE_PSK
};

wifiManager.setWifiProfile(wantTemp, profile).then(() => {
  console.info('Succeeded in setting wifi profile');
}).catch((err: BusinessError) => {
  console.error(`Failed to set wifi profile. Code: ${err.code}, message: ${err.message}`);
});
```
