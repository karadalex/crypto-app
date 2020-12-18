import * as React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Colors from '../constants/Colors';
import useColorScheme from '../hooks/useColorScheme';
import { BottomTabParamList } from '../types';
import TabBarIcon from '../components/Icon';

import Dashboard from '../screens/Dashboard';
import Prices from '../screens/Prices';
import Trade from '../screens/Trade';
import Portfolio from '../screens/Portfolio';
import Account from '../screens/Account';


const BottomTab = createBottomTabNavigator<BottomTabParamList>();

export default function BottomTabNavigator() {
  const colorScheme = useColorScheme();

  return (
    <BottomTab.Navigator
      initialRouteName="Dashboard"
      tabBarOptions={{ activeTintColor: Colors[colorScheme].tint }}
    >
      <BottomTab.Screen
        name="Dashboard"
        component={Dashboard}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="home-currency-usd" size={24} color={color} />,
        }}
      />
      <BottomTab.Screen
        name="Prices"
        component={Prices}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="coins" size={24} color={color} family="fa5" />,
        }}
      />
      <BottomTab.Screen
        name="Trade"
        component={Trade}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="exchange" size={28} color={color} family="fa" />,
        }}
      />
      <BottomTab.Screen
        name="Portfolio"
        component={Portfolio}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="finance" size={28} color={color} />,
        }}
      />
      <BottomTab.Screen
        name="Account"
        component={Account}
        options={{
          tabBarIcon: ({ color }) => <TabBarIcon name="person" size={28} color={color} family="material" />,
        }}
      />
    </BottomTab.Navigator>
  );
}

