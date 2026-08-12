# getInterceptedRecords (System API)

## Modules to Import

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## getInterceptedRecords

```TypeScript
function getInterceptedRecords(userId: number, requestParam: RequestParam): Promise<InterceptedRecordPage>
```

Get intercepted records by userId, and it is necessary to specify the pagination query parameters.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Required permissions:** ohos.permission.GET_NET_FIREWALL

<!--Device-netFirewall-function getInterceptedRecords(userId: number, requestParam: RequestParam): Promise<InterceptedRecordPage>--><!--Device-netFirewall-function getInterceptedRecords(userId: number, requestParam: RequestParam): Promise<InterceptedRecordPage>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetFirewall

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | Indicates the user ID. It cannot be the ID of a user that does not exist. |
| requestParam | [RequestParam](arkts-network-netfirewall-requestparam-i.md) | Yes | Paging query input parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[InterceptedRecordPage](arkts-network-netfirewall-interceptedrecordpage-i-sys.md)&gt; | Block Record List. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [29400000](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-netfirewall.md#29400000-specified-user-does-not-exist) | The specified user does not exist. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2100001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) | Operation failed. Cannot connect to service. |
| [2100003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let interceptRecordParam: netFirewall.RequestParam = {
  page: 1,
  pageSize: 10,
  orderField: netFirewall.NetFirewallOrderField.ORDER_BY_RECORD_TIME,
  orderType: netFirewall.NetFirewallOrderType.ORDER_DESC
};
netFirewall.getInterceptedRecords(100, interceptRecordParam).then((result: netFirewall.InterceptedRecordPage) => {
  console.info("result:", JSON.stringify(result));
}, (error: BusinessError) => {
  console.error("get intercept records failed: " + JSON.stringify(error));
});
```

