# startEthEap

## 导入模块

```TypeScript
import { eap } from '@kit.NetworkKit';
```

## startEthEap

```TypeScript
function startEthEap(netId: number, profile: EthEapProfile): void
```

该接口用于指定一个以太网卡发起EAP认证。

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为20。

**需要权限：** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

**系统能力：** SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| netId | number | 是 |
| profile | [EthEapProfile](arkts-network-eap-etheapprofile-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [33200001](../errorcode-net-eap.md#33200001-无效的netid值) |
| [33200003](../errorcode-net-eap.md#33200003-无效的eth-eap配置) |
| [33200009](../errorcode-net-eap.md#33200009-netmanager进程不存在) |
| [33200010](../errorcode-net-eap.md#33200010-无效的eth状态) |
| [33200099](../errorcode-net-eap.md#33200099-程序内部错误) |

**示例**

```TypeScript
import {eap} from '@kit.NetworkKit';
let netId = 100;
let profile: eap.EthEapProfile = {
  eapMethod: eap.EapMethod.EAP_TTLS,
  phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
  identity: "identity",
  anonymousIdentity: "anonymousIdentity",
  password: "password",
  caCertAliases: "caCertAliases",
  caPath: "caPath",
  clientCertAliases: "clientCertAliases",
  certEntry: new Uint8Array([5,6,7,8,9,10]),
  certPassword: "certPassword",
  altSubjectMatch: "altSubjectMatch",
  domainSuffixMatch: "domainSuffixMatch",
  realm: "realm",
  plmn: "plmn",
  eapSubId: 1
};
    
try {
  eap.startEthEap(netId, profile);
  console.info('startEthEap success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```
