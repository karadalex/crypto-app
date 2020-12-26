import * as React from 'react';
import { useQuery, gql } from '@apollo/client';
import { StyleSheet } from 'react-native';
import { Text, View } from '../components/Themed';


const USER_QUERY = gql`
  query Users {
    user(user_Id: 1) {
      email,
      firstName,
      lastName
    }
  }
`;

export default function Account() {
  const { loading, error, data } = useQuery(USER_QUERY);

  if (loading) return <Text>Loading...</Text>;
  if (error) return <Text>Error :(</Text>;
  
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Account</Text>
      <Text>{JSON.stringify(data.user)}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
