# @ohos.abilityToolAccessCtrl(This module provides the capabilities of tools access control)

The namespace of abilityToolAccessCtrl

**Since:** 26.0.0

**System capability:** SystemCapability.Security.Asset

**System API:** This is a system API.

## Modules to Import

```TypeScript
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [generateControlledDevicePackage(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-generatecontrolleddevicepackage-f-sys.md) | Generates an authorization package for the controlled device. This function generates a remote authorization package based on the permission query list. The generated package can be sent to the controller device for permission verification. |
| [generateControllerDevicePackage(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-generatecontrollerdevicepackage-f-sys.md) | Generates an authorization package for the controller device. This function generates a remote authorization package based on the remote user authorization results. The generated package can be sent to the controlled device for permission verification. |
| [getRemoteGrantStatus(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-getremotegrantstatus-f-sys.md) | Gets the remote grant status. This function queries whether the remote authorization feature is enabled or disabled. When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed. |
| [grantToolPermissionsByUser(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-granttoolpermissionsbyuser-f-sys.md) | Grants tool permissions based on user authorization results. This function grants permissions for tools (CLI commands or APIs) according to the user's authorization decisions. After successful authorization, tickets are generated which can be used for permission verification. |
| [requestToolPermissions(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-requesttoolpermissions-f-sys.md) | Queries tool permissions based on the specified operations. This function checks the permission status for CLI commands or APIs specified in permissionQuery.operationInfo. For each operation, it returns the permission status, authorization status, and whether a user dialog is required. When needTicket is set to true, a ticket will be generated for remote authorization. |
| [updateRemoteGrantStatus(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-updateremotegrantstatus-f-sys.md) | Updates the remote grant status. This function enables or disables the remote authorization feature. When enabled, the device can grant permissions to remote devices; when disabled, remote authorization is not allowed. |
| [verifyControlledDevicePackage(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-verifycontrolleddevicepackage-f-sys.md) | Verifies the authorization package from the controlled device. This function verifies the remote authorization package sent by the controlled device. It validates the ticket to ensure the authorization is legitimate. |
| [verifyControllerDevicePackage(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-verifycontrollerdevicepackage-f-sys.md) | Verifies the authorization package from the controller device. This function verifies the remote authorization package sent by the controller device. It validates the ticket and remote device information to ensure the authorization is legitimate. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AuthStatusInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-authstatusinfo-i-sys.md) | Authorization status information. |
| [CliCmdInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-clicmdinfo-i-sys.md) | CLI command information. |
| [OperationInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-operationinfo-i-sys.md) | Operation information. |
| [PermissionInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-permissioninfo-i-sys.md) | Permission information. |
| [PermissionQuery(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | Permission query information. |
| [PermissionQueryResult(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-permissionqueryresult-i-sys.md) | Permission query result. |
| [RemoteAuthPackage(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remoteauthpackage-i-sys.md) | Remote authorization package. |
| [RemoteControlParams(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remotecontrolparams-i-sys.md) | Interaction params for remote control |
| [RemoteInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remoteinfo-i-sys.md) | Remote device information. |
| [RemoteUserAuthItem(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remoteuserauthitem-i-sys.md) | Remote user authorization item. |
| [RemoteUserAuthResults(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remoteuserauthresults-i-sys.md) | Remote user authorization results. |
| [TicketInfo(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-ticketinfo-i-sys.md) | Ticket information. |
| [UserAuthResult(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-userauthresult-i-sys.md) | User authorization result. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [AuthStatus(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-authstatus-e-sys.md) | Authorization status. |
| [OperationType(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-operationtype-e-sys.md) | Operation type. |
| [RemoteGrantStatus(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-remotegrantstatus-e-sys.md) | Remote grant status. |
| [Role(This module provides the capabilities of tools access control)](arkts-ability-abilitytoolaccessctrl-role-e-sys.md) | Device role. |
<!--DelEnd-->
