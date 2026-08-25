# addNetFirewallRule

## 导入模块

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
```

## addNetFirewallRule

```TypeScript
function addNetFirewallRule(rule: NetFirewallRule): Promise<number>
```

添加系统用户ID的防火墙规则，目前支持的规则类型有：IP、Domain、DNS。使用Promise异步回调。

> **说明：**&gt;
> 1. 防火墙规则优先级说明（[setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md)和
> [addNetFirewallRule](#addnetfirewallrule)无调用顺序要求）：&gt;
> - 调用[setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md)设置默认策略为阻止，调用
> [addNetFirewallRule](#addnetfirewallrule)新增显式规则，规则优先级由高到低为：&gt;
> - 显式阻止规则&gt;
> - 显式允许规则&gt;
> - 默认阻止策略&gt;
> - 调用[setNetFirePolicy](arkts-network-netfirewall-setnetfirewallpolicy-f.md)设置默认策略为允许，调用
> [addNetFirewallRule](#addnetfirewallrule)新增显式规则，规则优先级由高到低为：&gt;
> - 显式允许规则&gt;
> - 显式阻止规则&gt;
> - 默认允许策略&gt;
> - 防火墙IP规则和域名规则冲突时（域名解析的IP与IP规则的IP相同，规则行为冲突）：&gt;
> - 若以域名方式访问，则域名规则优先级高于IP规则，不受域名解析出的IP的规则影响。&gt;
> - 若以IP方式访问，遵循以下原则：&gt;
> - 域名规则放行，若以IP方式访问之前经历过域名解析过程，则IP规则拦截或者默认策略拦截是不生效的，最终以IP方式访问是放行的。&gt;
> - 域名规则放行，若以IP方式访问之前未经历过域名解析过程，则IP规则拦截或者默认策略拦截是生效的，最终以IP方式访问是拦截的。&gt;
> - 域名规则拦截，则IP规则放行或者默认策略放行是生效的，最终以IP方式访问是放行的。&gt;
> 2. 规则类型补充说明：&gt;
> - 当addNetFirewallRule的入参rule.type配置为RULE_IP时：&gt;
> - 若rule.action为RULE_ALLOW，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段允许通行；&gt;
> - 若rule.action 为RULE_DENY，且rule.localIps、rule.remoteIps均不配置，规则生效为全IP段拦截。&gt;
> - 当addNetFirewallRule的入参rule.type配置为RULE_DOMAIN时，若rule.domains未配置，该规则不生效。&gt;
> 3. 防火墙规则添加上限说明：&gt;
> - 单个系统用户ID添加的防火墙规则上限是1000，若超过该上限，则报错29400001。&gt;
> - 所有的系统用户ID添加的防火墙规则总和的上限是2000，若超过该上限，则报错29400001。&gt;
> - 所有的系统用户ID添加的模糊域名规则总和的上限是100，若超过该上限，则报错29400005。

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为15。

**需要权限：** ohos.permission.MANAGE_NET_FIREWALL

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rule | [NetFirewallRule](arkts-network-netfirewall-netfirewallrule-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [29400000](../errorcode-net-netfirewall.md#29400000-指定用户不存在) |
| [29400001](../errorcode-net-netfirewall.md#29400001-防火墙规则数量超过最大值) |
| [29400002](../errorcode-net-netfirewall.md#29400002-防火墙规则中的ip地址规则数量超过最大值) |
| [29400003](../errorcode-net-netfirewall.md#29400003-防火墙规则中的port规则数量超过最大值) |
| [29400004](../errorcode-net-netfirewall.md#29400004-防火墙规则中的域名规则数量超过最大值) |
| [29400005](../errorcode-net-netfirewall.md#29400005-模糊域名规则数量超过最大值) |
| [29400007](../errorcode-net-netfirewall.md#29400007-dns规则重复) |

**示例**

```TypeScript
import { netFirewall } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ipRule: netFirewall.NetFirewallRule = {
  name: "rule1",
  description: "rule1 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_IP,
  isEnabled: true,
  appUid: 20001,
  localIps: [
    {
      family: 1,
      type: 1,
      address: "10.10.1.1",
      mask: 32
    },{
      family: 1,
      type: 2,
      startIp: "10.20.1.1",
      endIp: "10.20.1.10"
    }],
  remoteIps:[
    {
      family: 1,
      type: 1,
      address: "20.10.1.1",
      mask: 32
    },{
      family: 1,
      type: 2,
      startIp: "20.20.1.1",
      endIp: "20.20.1.10"
    }],
  protocol: 6,
  localPorts: [
    {
      startPort: 1000,
      endPort: 1000
    },{
      startPort: 2000,
      endPort: 2001
    }],
  remotePorts: [
    {
      startPort: 443,
      endPort: 443
    }],
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(ipRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let domainRule: netFirewall.NetFirewallRule = {
  name: "rule2",
  description: "rule2 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DOMAIN,
  isEnabled: true,
  appUid: 20002,
  domains: [
    {
      isWildcard: false,
      domain: "www.example.cn"
    },{
      isWildcard: true,
      domain: "*.example.cn"
    }],
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(domainRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});

let dnsRule: netFirewall.NetFirewallRule = {
  name: "rule3",
  description: "rule3 description",
  direction: netFirewall.NetFirewallRuleDirection.RULE_IN,
  action:netFirewall.FirewallRuleAction.RULE_DENY,
  type: netFirewall.NetFirewallRuleType.RULE_DNS,
  isEnabled: true,
  appUid: 20003,
  dns:{
   primaryDns: "4.4.4.4",
   standbyDns: "8.8.8.8",
  },
  userId: 100,
  interface:"wlan0" // 从API版本26.0.0开始支持
};
netFirewall.addNetFirewallRule(dnsRule).then((result: number) => {
  console.info('rule Id: ', result);
}, (reason: BusinessError) => {
  console.error('add firewall rule failed: ', JSON.stringify(reason));
});
```
